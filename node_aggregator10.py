from .core_lib import BasePromptAggregator

class PromptAggregator10(BasePromptAggregator):
    @classmethod
    def INPUT_TYPES(s):
        return s.create_input_types(10)
        