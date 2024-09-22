from pathlib import Path

import cv2
from insta_stories_cropper.app.exceptions import DirectoryNotFoundError
from insta_stories_cropper.app.parameters import Parameters
from insta_stories_cropper.cropper import Cropper
from insta_stories_cropper.face_detection.face_detector import FaceDetector
from insta_stories_cropper.face_detection.visualization import BoundingBoxDrawer
from insta_stories_cropper.timeCoherenceCorrector import TimeCoherenceCorrector


class App:
    def __init__(self, parameters: Parameters) -> None:
        self.time_coherence_history_threshold = (
            parameters.time_coherence_history_threshold
        )
        self.enable_bounding_box_drawing = parameters.enable_bounding_box_drawing

    def crop(
        self, input_filename: Path, output_filename: Path, ratio: list[int]
    ) -> None:
        # Capturing the first frame
        cap = cv2.VideoCapture(str(input_filename.absolute()))
        success, img = cap.read()
        # Capturing some frame information
        h_img, w_img, c_img = img.shape
        c_img = [int(w_img // 2), int(h_img // 2)]
        fps = cap.get(cv2.CAP_PROP_FPS)

        # Finding the size of the cropping given some ratio
        cropper = Cropper()
        cropper.findCropSize(ratio[0], ratio[1], w_img, h_img)
        print(int(cropper.width), int(cropper.height))

        # Time coherence corrector
        corrector = TimeCoherenceCorrector(c_img, self.time_coherence_history_threshold)

        # Initializing the face detector
        detector = FaceDetector()
        bounding_box_drawer = BoundingBoxDrawer()

        # Create a video writer to save the resulting video
        if not output_filename.parent.exists():
            raise DirectoryNotFoundError(output_filename.parent)

        video_writer = cv2.VideoWriter(
            str(output_filename),
            cv2.VideoWriter_fourcc(*"MJPG"),
            fps=fps,
            frameSize=(int(cropper.width), int(cropper.height)),
        )

        while True:
            if not success:
                break

            bounding_boxes = detector.detect(img)

            if self.enable_bounding_box_drawing:
                img = bounding_box_drawer.draw(img, bounding_boxes)

            # When no face detections
            if not bounding_boxes:
                c_bbox = c_img
                img = cropper.crop(img, c_bbox)

            else:
                # Only for the first detection
                for bbox in bounding_boxes:
                    c_bbox = corrector.correct(bbox.center)

                    img = cropper.crop(img, c_bbox)

                    # By the moment, only for the first face detected
                    break
            video_writer.write(img)
            cv2.imshow("Image", img)
            cv2.waitKey(1)

            # Read next frame
            success, img = cap.read()

        cap.release()
        video_writer.release()

        cv2.destroyAllWindows()
