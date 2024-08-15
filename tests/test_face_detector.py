import os
from pathlib import Path

import cv2
import numpy as np
from insta_stories_cropper.face_detection.face_detector import BoundingBox
from insta_stories_cropper.face_detection.face_detector import FaceDetector

BASE_PATH = Path(os.path.dirname(__file__))
ONE_FACE_IMAGE_PATH = str(BASE_PATH / "resources/one_face.jpg")
TWO_FACE_IMAGE_PATH = str(BASE_PATH / "resources/two_faces.jpg")


def test_detect_one_face():
    detector = FaceDetector()

    img = cv2.imread(ONE_FACE_IMAGE_PATH)

    bounding_boxes = detector.detect(img)

    expected_number_detections = 1
    assert expected_number_detections == len(bounding_boxes)

    bounding_box_0 = bounding_boxes[0]
    expected_bounding_box = BoundingBox(368, 105, 133, 133)
    assert expected_bounding_box == bounding_box_0


def test_detect_two_faces():
    detector = FaceDetector()

    img = cv2.imread(TWO_FACE_IMAGE_PATH)

    bounding_boxes = detector.detect(img)

    expected_number_detections = 2
    assert expected_number_detections == len(bounding_boxes)

    bounding_box_0 = bounding_boxes[0]
    expected_bounding_box = BoundingBox(81, 114, 167, 167)
    assert expected_bounding_box == bounding_box_0

    bounding_box_1 = bounding_boxes[1]
    expected_bounding_box = BoundingBox(232, 236, 171, 171)
    assert expected_bounding_box == bounding_box_1


def test_detect_no_faces():
    detector = FaceDetector()

    img = np.zeros([100, 100, 3], dtype=np.uint8)

    bounding_boxes = detector.detect(img)

    expected_number_detections = 0
    assert expected_number_detections == len(bounding_boxes)
