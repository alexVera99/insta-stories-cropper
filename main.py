import FaceDetectionModule
import cv2
import CropModule

# Capturing the first frame
cap = cv2.VideoCapture("videos/music_video.mp4")
success, img = cap.read()
# Capturing some frame information
h_img, w_img, c_img = img.shape
c_img = [int(w_img//2), int(h_img//2)]

# Finding the size of the cropping given some ratio
ratio = [9, 16] # [w, h]
cropper = CropModule.CropModule()
cropper.findCropSize(ratio[0], ratio[1], w_img, h_img)

# Initializing the face detector
detector = FaceDetectionModule.faceDetector()

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

