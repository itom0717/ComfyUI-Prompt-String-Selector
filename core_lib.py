import os
import re
import json

CATEGORY_TEXT = "Prompt String Selector"


class ConfigManager:
    @classmethod
    def get_plugin_dir(cls):
        return os.path.dirname(os.path.realpath(__file__))

    @classmethod
    def get_config_files(cls):
        """プラグインディレクトリ内の config*.json または configs/ 内の *.json を取得"""
        plugin_dir = cls.get_plugin_dir()
        configs = []

        # 1. ルートディレクトリの config*.json
        for f in os.listdir(plugin_dir):
            if f.startswith("config") and f.endswith(".json"):
                configs.append(f)

        # 2. サブディレクトリ configs/ がある場合はその中の json も対象にする
        configs_dir = os.path.join(plugin_dir, "configs")
        if os.path.exists(configs_dir) and os.path.isdir(configs_dir):
            for f in os.listdir(configs_dir):
                if f.endswith(".json"):
                    configs.append(os.path.join("configs", f))

        configs.sort()
        return configs if configs else ["config.json"]

    @classmethod
    def get_base_data_path(cls, config_name="config.json"):
        plugin_dir = cls.get_plugin_dir()
        base_data_path = os.path.join(plugin_dir, "data")

        config_path = os.path.join(plugin_dir, config_name)
        if os.path.exists(config_path):
            try:
                with open(config_path, "r", encoding="utf-8") as f:
                    config = json.load(f)
                    custom_path = config.get("data_path", "").strip()
                    if custom_path:
                        base_data_path = (
                            custom_path
                            if os.path.isabs(custom_path)
                            else os.path.abspath(os.path.join(plugin_dir, custom_path))
                        )
            except Exception:
                pass
        return base_data_path


class BasePromptSelector:
    # 各子クラスで上書きされる定数
    FOLDER_NAME = ""
    L_SELECT = "select"
    L_CUSTOM = "custom"
    CONFIG_SELECT = "config_profile"

    @classmethod
    def get_file_list(cls, subfolder, config_name="config.json"):
        base_path = ConfigManager.get_base_data_path(config_name)
        folder_path = os.path.join(base_path, subfolder)
        os.makedirs(folder_path, exist_ok=True)
        files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]
        if not files:
            return ["custom_input"]

        def extract_sort_key(filename):
            match = re.match(r"(\d+)_", filename)
            return int(match.group(1)) if match else 999999

        files.sort(key=extract_sort_key)
        return [os.path.splitext(f)[0] for f in files] + ["custom_input"]

    RETURN_TYPES = ("STRING", "INT")
    RETURN_NAMES = ("text", "id")
    FUNCTION = "execute"
    CATEGORY = CATEGORY_TEXT

    @classmethod
    def INPUT_TYPES(cls):
        config_files = ConfigManager.get_config_files()
        default_config = config_files[0]

        return {
            "required": {
                # 設定JSONファイルを切り替えるためのドロップダウン
                cls.CONFIG_SELECT: (config_files, {"default": default_config}),
                cls.L_SELECT: (cls.get_file_list(cls.FOLDER_NAME, default_config),),
                cls.L_CUSTOM: ("STRING", {"default": "", "multiline": True}),
            }
        }

    def clean_comment(self, text):
        text = re.sub(r"/\*.*?\*/", "", text, flags=re.DOTALL)
        text = re.sub(r"//.*", "", text)
        lines = [l.strip() for l in text.splitlines() if l.strip()]
        return " ".join(lines).strip().rstrip(",")

    def execute(self, **kwargs):
        selection = kwargs.get(self.L_SELECT)
        custom_text = kwargs.get(self.L_CUSTOM)
        config_name = kwargs.get(self.CONFIG_SELECT, "config.json")

        txt, idx = self.execute_logic(selection, custom_text, self.FOLDER_NAME, config_name)
        if txt:
            txt += ",\n"
        return (txt, idx)

    def execute_logic(self, selection, custom_text, subfolder, config_name):
        match = re.match(r"(\d+)_", selection)
        selected_id = int(match.group(1)) if match else 0
        raw_text = ""
        if selection == "custom_input":
            raw_text = custom_text
        else:
            base_path = ConfigManager.get_base_data_path(config_name)
            path = os.path.join(base_path, subfolder, f"{selection}.txt")
            try:
                with open(path, "r", encoding="utf-8") as f:
                    raw_text = f.read()
            except Exception:
                pass
        return (self.clean_comment(raw_text), selected_id)


class BaseBasePromptSwitch:
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("selected_text",)
    FUNCTION = "execute"
    CATEGORY = CATEGORY_TEXT

    @classmethod
    def create_input_types(cls, count):
        optional_inputs = {}
        for i in range(1, count + 1):
            name = f"text_{i:02d}"
            optional_inputs[name] = ("STRING", {"forceInput": True})

        return {
            "required": {
                "id": ("INT", {"default": 1, "min": 1, "max": count}),
            },
            "optional": optional_inputs,
        }

    def execute(self, id, **kwargs):
        target_name = f"text_{id:02d}"
        val = kwargs.get(target_name)

        selected_text = ""
        if val is not None and isinstance(val, str) and val.strip():
            selected_text = val.strip()
            if not selected_text.endswith(","):
                selected_text += ",\n"
            else:
                selected_text += "\n"

        return (selected_text,)


class BasePromptAggregator:
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("combined_prompt",)
    FUNCTION = "aggregate"
    CATEGORY = CATEGORY_TEXT

    @classmethod
    def create_input_types(cls, count):
        optional_inputs = {}
        for i in range(1, count + 1):
            name = f"text_{i:02d}"
            optional_inputs[name] = ("STRING", {"forceInput": True, "default": ""})
        return {"required": {}, "optional": optional_inputs}

    def aggregate(self, **kwargs):
        active_prompts = []
        sorted_keys = sorted([k for k in kwargs.keys() if k.startswith("text_")])
        for name in sorted_keys:
            val = kwargs.get(name)
            if val is not None and isinstance(val, str) and val.strip():
                cleaned = val.strip()
                if not cleaned.endswith(","):
                    cleaned += ","
                active_prompts.append(cleaned)

        return ("\n".join(active_prompts),)


class BaseIdSelector:
    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("id",)
    FUNCTION = "execute"
    CATEGORY = CATEGORY_TEXT

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "id": ("INT", {"default": 1, "min": 1, "max": 999999}),
                "memo": ("STRING", {"default": "", "multiline": True}),
            }
        }

    def execute(self, id, memo):
        return (id,)