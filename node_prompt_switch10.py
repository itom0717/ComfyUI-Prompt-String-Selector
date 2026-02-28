from .core_lib import BaseBasePromptSwitch

class PromptSwitch10(BaseBasePromptSwitch):
    @classmethod
    def INPUT_TYPES(s):
        return s.create_input_types(10)
        