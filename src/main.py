import cv2
import faceDetector
import numpy as np
from cropper import Cropper
from timeCoherenceCorrector import TimeCoherenceCorrector


def main() -> None:
    # Parameters
    ratio = [9, 16]  # [w, h]
    th = 50
    filename = "../videos/1.mp4"

    # Capturing the first frame
    cap = cv2.VideoCapture(filename)
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
    corrector = TimeCoherenceCorrector(c_img, th)

    # Initializing the face detector
    detector = faceDetector.faceDetector()

    # Create a video writer to save the resulting video
    video_writer = cv2.VideoWriter(
        "videos/output/filename.avi",
        cv2.VideoWriter_fourcc(*"MJPG"),
        fps=fps,
        frameSize=(int(cropper.width), int(cropper.height)),
    )

    while True:
        if not success:
            break

        img, bboxs = detector.findFaces(img, False)

        # When no face detections
        if bboxs == []:
            c_bbox = c_img
            img = cropper.crop(img, c_bbox)

        else:
            # Only for the first detection
            for bbox in bboxs:
                cur_c_bbox = np.array(bbox[2])

                c_bbox = corrector.correct(cur_c_bbox)

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


if __name__ == "__main__":
    main()
