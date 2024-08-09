import numpy as np


class TimeCoherenceCorrector:
    def __init__(self, center_image: int, threshold: int = 50):
        self.c_bboxs_hist = np.array([center_image])
        self.th = threshold

    def correct(self, cur_c_bbox: np.ndarray) -> np.ndarray:
        # cur_c_bbox is expected to be a numpy array of dimensions (2,)
        dist = np.linalg.norm(cur_c_bbox - self.c_bboxs_hist[-1], 2)

        if dist > self.th:
            self.c_bboxs_hist = np.array([cur_c_bbox])
        else:
            self.c_bboxs_hist = np.append(self.c_bboxs_hist, [cur_c_bbox], axis=0)

        return np.mean(self.c_bboxs_hist, axis=0, dtype=int)
