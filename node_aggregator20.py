from .core_lib import BasePromptAggregator

class PromptAggregator20(BasePromptAggregator):
    @classmethod
    def INPUT_TYPES(s):
        return s.create_input_types(20)
        