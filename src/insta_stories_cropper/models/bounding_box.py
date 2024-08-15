from dataclasses import dataclass


@dataclass
class BoundingBox:
    # left
    x_min: int
    # top
    y_min: int
    height: int
    width: int

    @property
    def center(self) -> list[int]:
        return [self.x_min + self.width // 2, self.y_min + self.height // 2]
