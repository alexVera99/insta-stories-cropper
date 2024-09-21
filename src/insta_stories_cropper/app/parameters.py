from dataclasses import dataclass


@dataclass
class Parameters:
    time_coherence_history_threshold: int = 50
    enable_bounding_box_drawing: bool = False
