import os
import re
import json

# カテゴリー名を定数として定義
CATEGORY_TEXT = "Prompt String Selector"


class BasePromptSelector:
    @classmethod
    def get_base_data_path(cls):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        base_data_path = os.path.join(current_dir, "data")
        config_path = os.path.join(current_dir, "config.json")
        if os.path.exists(config_path):
            try:
                with open(config_path, "r", encoding="utf-8") as f:
                    config = json.load(f)
                    custom_path = config.get("data_path", "").strip()
                    if custom_path:
                        base_data_path = custom_path if os.path.isabs(custom_path) else os.path.abspath(os.path.join(current_dir, custom_path))
            except: pass
        return base_data_path

    @classmethod
    def get_file_list(cls, subfolder):
        base_path = cls.get_base_data_path()
        folder_path = os.path.join(base_path, subfolder)
        os.makedirs(folder_path, exist_ok=True)
        files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]
        if not files: return ["custom_input"]
        def extract_sort_key(filename):
            match = re.match(r'(\d+)_', filename)
            return int(match.group(1)) if match else 999999
        files.sort(key=extract_sort_key)
        return [os.path.splitext(f)[0] for f in files] + ["custom_input"]

    RETURN_TYPES = ("STRING", "INT")
    RETURN_NAMES = ("text", "id")
    FUNCTION = "execute"
    CATEGORY = CATEGORY_TEXT

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            cls.L_SELECT: (cls.get_file_list(cls.FOLDER_NAME),),
            cls.L_CUSTOM: ("STRING", {"default": "", "multiline": True})
        }}

    def clean_comment(self, text):
        text = re.sub(r'/\*.*?\*/', '', text, flags=re.DOTALL)
        text = re.sub(r'//.*', '', text)
        lines = [l.strip() for l in text.splitlines() if l.strip()]
        return " ".join(lines).strip().rstrip(",")

    def execute(self, **kwargs):
        selection = kwargs.get(self.L_SELECT)
        custom_text = kwargs.get(self.L_CUSTOM)
        txt, idx = self.execute_logic(selection, custom_text, self.FOLDER_NAME)
        if txt: txt += ",\n"
        return (txt, idx)

    def execute_logic(self, selection, custom_text, subfolder):
        match = re.match(r'(\d+)_', selection)
        selected_id = int(match.group(1)) if match else 0
        raw_text = ""
        if selection == "custom_input":
            raw_text = custom_text
        else:
            path = os.path.join(self.get_base_data_path(), subfolder, f"{selection}.txt")
            try:
                with open(path, "r", encoding="utf-8") as f:
                    raw_text = f.read()
            except: pass
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
            "optional": optional_inputs
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
        # kwargsに入っているすべての text_XX を順番に処理
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
    def INPUT_TYPES(s):
        return {
            "required": {
                "id": ("INT", {"default": 1, "min": 1, "max": 999999}),
                "memo": ("STRING", {"default": "", "multiline": True}),
            }
        }

    def execute(self, id, memo):
        return (id,)


