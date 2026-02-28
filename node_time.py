from .core_lib import BasePromptSelector

class TimeSelector(BasePromptSelector):
    FOLDER_NAME = "time"
    L_SELECT    = "time"
    L_CUSTOM    = "time_custom"