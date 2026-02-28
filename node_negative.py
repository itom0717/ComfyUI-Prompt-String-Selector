from .core_lib import BasePromptSelector

class NegativeSelector(BasePromptSelector):
    FOLDER_NAME = "negative"
    L_SELECT    = "negative"
    L_CUSTOM    = "negative_custom"