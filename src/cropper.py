from math import floor

import numpy as np


class Cropper:
    def findCropSize(
        self, width: int, height: int, img_width: int, img_height: int
    ) -> None:
        ratio = width / height
        if img_width >= img_height:
            self.height = img_height
            self.width = floor(ratio * img_height)
        else:
            self.width = img_width
            self.height = floor(img_height / ratio)

    def limitInBoundaries(
        self,
        img_width: int,
        img_height: int,
        x_min: int,
        y_min: int,
        x_max: int,
        y_max: int,
    ) -> tuple[int, int, int, int]:
        if x_min < 0:
            x_max = self.width - 1
            x_min = 0
        if y_min < 0:
            y_max = self.height - 1
            y_min = 0
        if x_max > img_width:
            x_min = img_width - self.width
            x_max = img_width - 1
        if y_max > img_height:
            y_min = img_height - self.height
            y_max = img_height - 1

        return x_min, y_min, x_max, y_max

    def crop(self, img: np.ndarray, center: list[int]) -> np.ndarray:
        img_height, img_width, _ = img.shape

        x_min = center[0] - int(self.width // 2)
        y_min = center[1] - int(self.height // 2)
        x_max = center[0] + int(self.width // 2)
        y_max = center[1] + int(self.height // 2)

        x_min, y_min, x_max, y_max = self.limitInBoundaries(
            img_width, img_height, x_min, y_min, x_max, y_max
        )
        # print(self.x_min, self.x_max, self.y_min, self.y_max)

        return img[y_min : y_max + 1, x_min : x_max + 1, :]
