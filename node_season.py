from .core_lib import BasePromptSelector

class SeasonSelector(BasePromptSelector):
    FOLDER_NAME = "season"
    L_SELECT    = "season"
    L_CUSTOM    = "season_custom"