import cv2
import numpy as np
from insta_stories_cropper.models.bounding_box import BoundingBox


class BoundingBoxDrawer:
    def draw(self, image: np.ndarray, bounding_boxes: list[BoundingBox]) -> np.ndarray:
        for bounding_box in bounding_boxes:
            image = self._draw_bounding_box(image, bounding_box)

        return image

    def _draw_bounding_box(
        self, image: np.ndarray, bounding_box: BoundingBox
    ) -> np.ndarray:
        top_left = [bounding_box.x_min, bounding_box.y_min]
        bottom_right = [
            bounding_box.x_min + bounding_box.width,
            bounding_box.y_min + bounding_box.height,
        ]

        cv2.rectangle(image, top_left, bottom_right, (255, 0, 0), 2)

        return image
