import FaceDetectionModule
import cv2
import CropModule
import numpy as np

# Capturing the first frame
cap = cv2.VideoCapture("videos/1.mp4")
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

# Time consistency parameters
th = 2800
mean_c_bboxs = np.array(c_img)

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
            cur_c_bbox = bbox[2]
            cur_mean_c_bbox = [cur_c_bbox, mean_c_bboxs]
            print("Current_pos: " + str(cur_c_bbox))
            print("Mean: " + str(mean_c_bboxs))
            dist = np.linalg.norm(cur_c_bbox, 2)

            if(dist > th):
                mean_c_bboxs = cur_c_bbox
            else:
                mean_c_bboxs = np.mean(cur_mean_c_bbox, axis=0)

            print("Dist: " + str(dist))
            #c_bbox = bbox[2]
            c_bbox = list(map(int,mean_c_bboxs))
            print("Box pos " + str(c_bbox) + "\n\n")
            img = cropper.crop(img, c_bbox)
            # By the moment, only for the first face detected
            break

    cv2.imshow("Image", img)
    cv2.waitKey(1)

    # Read next frame
    success, img = cap.read()

