import cv2
import numpy as np
from insta_stories_cropper.models.bounding_box import BoundingBox
from mediapipe.python.solutions.face_detection import (
    FaceDetection as MediapipeFaceDetector,
)
from mediapipe.tasks.python.components.containers.detections import Detection


class FaceDetector:
    def __init__(self, minimum_detection_confidence: float = 0.5):
        self.face_detector = MediapipeFaceDetector(minimum_detection_confidence)

    def detect(self, img: np.ndarray) -> list[BoundingBox]:
        image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        detections = self.face_detector.process(image_rgb).detections

        bounding_boxes = []

        if not detections:
            return []

        image_height, image_width, _ = img.shape

        for detection in detections:
            bounding_boxes.append(
                self._parse_detections(detection, image_width, image_height)
            )

        return bounding_boxes

    @staticmethod
    def _parse_detections(
        detection: Detection, image_width: int, image_height: int
    ) -> BoundingBox:
        relative_bounding_box = detection.location_data.relative_bounding_box

        return BoundingBox(
            int(relative_bounding_box.xmin * image_width),
            int(relative_bounding_box.ymin * image_height),
            int(relative_bounding_box.width * image_width),
            int(relative_bounding_box.height * image_height),
        )
