import faceDetector
import cv2
import cropper
import numpy as np
from timeCoherenceCorrector import TimeCoherenceCorrector

# Parameters
ratio = [9, 16] # [w, h]
th = 50
filename = "videos/1.mp4"

# Capturing the first frame
cap = cv2.VideoCapture(filename)
success, img = cap.read()
# Capturing some frame information
h_img, w_img, c_img = img.shape
c_img = [int(w_img//2), int(h_img//2)]

# Finding the size of the cropping given some ratio
cropper = cropper.Cropper()
cropper.findCropSize(ratio[0], ratio[1], w_img, h_img)

# Time coherence corrector
corrector = TimeCoherenceCorrector(c_img, th)

# Initializing the face detector
detector = faceDetector.faceDetector()

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
            cur_c_bbox = np.array(bbox[2])
            
            c_bbox = corrector.correct(cur_c_bbox)

            img = cropper.crop(img, c_bbox)
            
            # By the moment, only for the first face detected
            break

    cv2.imshow("Image", img)
    cv2.waitKey(1)

    # Read next frame
    success, img = cap.read()

