import FaceDetectionModule
import cv2
import CropModule
import numpy as np

# Capturing the first frame
cap = cv2.VideoCapture("videos/music_video_2.mp4")
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
th = 50
c_bboxs_hist = np.array([c_img])

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
            print("Current_pos: " + str(cur_c_bbox))
            dist = np.linalg.norm(cur_c_bbox - c_bboxs_hist[-1], 2)

            if(dist > th):
                c_bboxs_hist = np.array([cur_c_bbox])
            else:
                c_bboxs_hist = np.append(c_bboxs_hist, [cur_c_bbox], axis=0)

            print("Dist: " + str(dist))
            c_bbox = np.mean(c_bboxs_hist, axis=0, dtype=int)
            print("Box pos " + str(c_bbox) + "\n\n")
            img = cropper.crop(img, c_bbox)
            # By the moment, only for the first face detected
            break

    cv2.imshow("Image", img)
    cv2.waitKey(1)

    # Read next frame
    success, img = cap.read()

