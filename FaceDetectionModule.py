
import cv2
import mediapipe as mp
import time

class faceDetector():
    def __init__(self, minDetectionCon = 0.5):
        self.minDetectionCon = minDetectionCon

        self.mpFaceDetection = mp.solutions.face_detection
        self.mp_drawing = mp.solutions.drawing_utils
        self.faceDetection = self.mpFaceDetection.FaceDetection(self.minDetectionCon)

    def findFaces(self, img, draw = False):
        # bboxs: it's a list with the following information of each face detection
        # id, bbox, center_bbox, score
        img.flags.writeable = False
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        self.results = self.faceDetection.process(imgRGB)

        bboxs = []

        if self.results.detections:
            for id, detection in enumerate(self.results.detections):
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, ic = img.shape
                bbox = int(bboxC.xmin * iw ), int(bboxC.ymin * ih ), int(bboxC.width * iw ), int(bboxC.height * ih ) 
                
                center_bbox = self.findCenterBbox(bbox)

                bboxs.append([id, bbox, center_bbox, detection.score])

                if draw:
                    img = self.debug(img, id, detection, bbox)

        return img, bboxs

    def findCenterBbox(self, bbox):
        x_min, y_min, w, h = bbox
        x_max = x_min + w
        y_max = y_min + h
        
        center = [int((x_max + x_min)//2), int((y_max + y_min)//2)] 

        return center
    
    def debug(self, img, id, detection, bbox):
        img.flags.writeable = True

        self.mp_drawing.draw_detection(img, detection)

        print(bbox[0], bbox[1])
        cv2.putText(img, f'ID: {int(id)}', (bbox[0], bbox[1]), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 3)
        return img





def main():
    cap = cv2.VideoCapture("videos/1.mp4")
    # cap = cv2.VideoCapture(0)

    pTime = 0

    detector = faceDetector()

    while True:
        success, img = cap.read()

        img, bboxs, c_bbox = detector.findFaces(img, True)

        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 3)
        

        cv2.imshow("Image", img)
        cv2.waitKey(1)



if __name__ == "__main__":
    main()