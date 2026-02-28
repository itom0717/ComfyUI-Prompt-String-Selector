from .core_lib import BaseBasePromptSwitch

class PromptSwitch20(BaseBasePromptSwitch):
    @classmethod
    def INPUT_TYPES(s):
        return s.create_input_types(20)
        