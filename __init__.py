from .node_art_style       import ArtStyleSelector
from .node_character       import CharacterSelector
from .node_emotion         import EmotionSelector
from .node_pose1           import Pose1Selector
from .node_pose2           import Pose2Selector
from .node_clothing1       import Clothing1Selector
from .node_clothing2       import Clothing2Selector
from .node_clothing3       import Clothing3Selector
from .node_clothing4       import Clothing4Selector
from .node_season          import SeasonSelector
from .node_time            import TimeSelector
from .node_background      import BackgroundSelector
from .node_camera          import CameraSelector
from .node_extra1          import Extra1Selector
from .node_extra2          import Extra2Selector
from .node_extra3          import Extra3Selector
from .node_extra4          import Extra4Selector
from .node_extra5          import Extra5Selector
from .node_negative        import NegativeSelector
from .node_aggregator10    import PromptAggregator10
from .node_aggregator20    import PromptAggregator20
from .node_id_selector     import IdSelector
from .node_prompt_switch5  import PromptSwitch5
from .node_prompt_switch10 import PromptSwitch10
from .node_prompt_switch20 import PromptSwitch20

PFIX = "itom_PromptStringSelector_"

NODE_CLASS_MAPPINGS = {
    f"{PFIX}ArtStyleSelector":   ArtStyleSelector,
    f"{PFIX}CharacterSelector":  CharacterSelector,
    f"{PFIX}EmotionSelector":    EmotionSelector,
    f"{PFIX}Pose1Selector":      Pose1Selector,
    f"{PFIX}Pose2Selector":      Pose2Selector,
    f"{PFIX}Clothing1Selector":  Clothing1Selector,
    f"{PFIX}Clothing2Selector":  Clothing2Selector,
    f"{PFIX}Clothing3Selector":  Clothing3Selector,
    f"{PFIX}Clothing4Selector":  Clothing4Selector,
    f"{PFIX}SeasonSelector":     SeasonSelector,
    f"{PFIX}TimeSelector":       TimeSelector,
    f"{PFIX}BackgroundSelector": BackgroundSelector,
    f"{PFIX}CameraSelector":     CameraSelector,
    f"{PFIX}Extra1Selector":     Extra1Selector,
    f"{PFIX}Extra2Selector":     Extra2Selector,
    f"{PFIX}Extra3Selector":     Extra3Selector,
    f"{PFIX}Extra4Selector":     Extra4Selector,
    f"{PFIX}Extra5Selector":     Extra5Selector,
    f"{PFIX}NegativeSelector":   NegativeSelector,
    f"{PFIX}PromptAggregator10": PromptAggregator10,
    f"{PFIX}PromptAggregator20": PromptAggregator20,
    f"{PFIX}IdSelector":         IdSelector,
    f"{PFIX}PromptSwitch5":      PromptSwitch5,
    f"{PFIX}PromptSwitch10":     PromptSwitch10,
    f"{PFIX}PromptSwitch20":     PromptSwitch20
}

NODE_DISPLAY_NAME_MAPPINGS = {
    f"{PFIX}ArtStyleSelector":   "Art Style",
    f"{PFIX}CharacterSelector":  "Character",
    f"{PFIX}EmotionSelector":    "Emotion",
    f"{PFIX}Pose1Selector":      "Pose 1",
    f"{PFIX}Pose2Selector":      "Pose 2",
    f"{PFIX}Clothing1Selector":  "Clothing 1",
    f"{PFIX}Clothing2Selector":  "Clothing 2",
    f"{PFIX}Clothing3Selector":  "Clothing 3",
    f"{PFIX}Clothing4Selector":  "Clothing 4",
    f"{PFIX}SeasonSelector":     "Season",
    f"{PFIX}TimeSelector":       "Time",
    f"{PFIX}BackgroundSelector": "Background",
    f"{PFIX}CameraSelector":     "Camera",
    f"{PFIX}Extra1Selector":     "Extra 1",
    f"{PFIX}Extra2Selector":     "Extra 2",
    f"{PFIX}Extra3Selector":     "Extra 3",
    f"{PFIX}Extra4Selector":     "Extra 4",
    f"{PFIX}Extra5Selector":     "Extra 5",
    f"{PFIX}NegativeSelector":   "Negative",
    f"{PFIX}PromptAggregator10": "Aggregator (10)",
    f"{PFIX}PromptAggregator20": "Aggregator (20)",
    f"{PFIX}IdSelector":         "ID Select",
    f"{PFIX}PromptSwitch5":      "Prompt Switch (5)",
    f"{PFIX}PromptSwitch10":     "Prompt Switch (10)",
    f"{PFIX}PromptSwitch20":     "Prompt Switch (20)"
}