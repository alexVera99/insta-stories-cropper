from dataclasses import dataclass


@dataclass
class Parameters:
    time_coherence_history_threshold: int = 50
