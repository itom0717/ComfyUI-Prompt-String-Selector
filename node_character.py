from .core_lib import BasePromptSelector

class CharacterSelector(BasePromptSelector):
    FOLDER_NAME = "character"
    L_SELECT    = "character"
    L_CUSTOM    = "character_custom"