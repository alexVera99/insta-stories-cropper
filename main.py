import FaceDetectionModule
import cv2
import CropModule

cap = cv2.VideoCapture("videos/music_video.mp4")

detector = FaceDetectionModule.faceDetector()
cropper = CropModule.CropModule()

success, img = cap.read()

h_img, w_img, c_img = img.shape
c_img = [int(w_img//2), int(h_img//2)]

cropper.findCropSize(9, 16, w_img, h_img)

while True:
    if(not success):
        break

    img, bboxs = detector.findFaces(img, False)

    # When no face detections
    if(bboxs == []):
        c_bbox = c_img
        img = cropper.crop(img, c_bbox)
    
    else:
        # Only for the first detection
        for bbox in bboxs:
            c_bbox = bbox[2]
            img = cropper.crop(img, c_bbox)
            # By the moment, only for the first face detected
            break

    cv2.imshow("Image", img)
    cv2.waitKey(1)

    # Read next frame
    success, img = cap.read()

