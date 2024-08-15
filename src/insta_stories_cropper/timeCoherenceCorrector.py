import numpy as np


class TimeCoherenceCorrector:
    def __init__(self, center_image: int, threshold: int = 50):
        self.c_bboxs_hist = np.array([center_image])
        self.th = threshold

    def correct(self, current_center_bbox: list[int]) -> list[int]:
        # cur_c_bbox is expected to be a numpy array of dimensions (2,)
        current_center_bbox_ndarray = np.array(current_center_bbox)
        dist = np.linalg.norm(current_center_bbox_ndarray - self.c_bboxs_hist[-1], 2)

        if dist > self.th:
            self.c_bboxs_hist = np.array([current_center_bbox_ndarray])
        else:
            self.c_bboxs_hist = np.append(
                self.c_bboxs_hist, [current_center_bbox_ndarray], axis=0
            )

        return list(np.mean(self.c_bboxs_hist, axis=0, dtype=int))
