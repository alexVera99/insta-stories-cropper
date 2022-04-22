import faceDetector
import cv2
import cropper
import numpy as np
from timeCoherenceCorrector import TimeCoherenceCorrector
import audio_extractor
import video_merger
import bash_executor

# Parameters
ratio = [9, 16] # [w, h]
th = 50
input_video_filename = "videos/large_videos/music_video_2.mp4"

# Capturing the first frame
cap = cv2.VideoCapture(input_video_filename)
success, img = cap.read()
# Capturing some frame information
h_img, w_img, c_img = img.shape
c_img = [int(w_img//2), int(h_img//2)]
fps = cap.get(cv2.CAP_PROP_FPS)

# Finding the size of the cropping given some ratio
cropper = cropper.Cropper()
cropper.findCropSize(ratio[0], ratio[1], w_img, h_img)
print(int(cropper.width), int(cropper.height))

# Time coherence corrector
corrector = TimeCoherenceCorrector(c_img, th)

# Initializing the face detector
detector = faceDetector.faceDetector()

# Create a video writer to save the resulting video
output_video_filename = 'videos/output/output.avi'
video_writer = cv2.VideoWriter(output_video_filename,
                                cv2.VideoWriter_fourcc(*'MJPG'),
                                fps=fps, frameSize=(int(cropper.width), int(cropper.height)))

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
    video_writer.write(img)
    #cv2.imshow("Image", img)
    #cv2.waitKey(1)

    # Read next frame
    success, img = cap.read()

cap.release()
video_writer.release()

cv2.destroyAllWindows()

# Extract audio from the original video
output_audio_filename = 'temp.aac'
my_audio_extractor = audio_extractor.AudioExtractor()
my_audio_extractor.extract_audio(input_video_filename, output_audio_filename)

# Merge audio to the new video
output_final_video = 'videos/output/output_video_audio.mp4'
my_video_audio_merger = video_merger.VideoMerger()
my_video_audio_merger.merge_video_and_audio(output_video_filename, output_audio_filename, output_final_video)

# Remove the extracted audio file
my_bash_executor = bash_executor.BashExecutor()
my_bash_executor.executeCommand(f"rm {output_audio_filename}")
# Remove the extracted video file without audio
my_bash_executor.executeCommand(f"rm {output_video_filename}")