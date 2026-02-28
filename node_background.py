from .core_lib import BasePromptSelector

class BackgroundSelector(BasePromptSelector):
    FOLDER_NAME = "background"
    L_SELECT    = "background"
    L_CUSTOM    = "background_custom"