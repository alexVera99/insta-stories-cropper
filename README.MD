# Description
This project borns while using the videos in Spotify. You may have seen that while listening some songs, the original video of the song appears also. The point is that such videos where not edited for 9:16 ratio displays (in other words, mobile displays in vertical). And, those videos were showing the faces of the people that were in the video singing. 

But, the point is that manually editing a video to follow faces is not a nice task. Then, I asked myself how do the people at Spotify did this.

So, here it is. This project aims to crop a video following faces. In fact, it can be used to any w:h ratio, where w is width and h is height.

For instance, imagine you have this video:
<p align="center">
  <img style="width: 25em;" src="videos/demo/video_demo_1.gif" alt="Video by Assad Tanoli from Pexels"/>
</p>

Then, the output should be this video:
<p align="center">
  <img style="height: 25em;" src="videos/demo/video_demo_1_cropped.gif" alt="Video by Assad Tanoli from Pexels. It has been cropped with a ratio of 9:16."/>
</p>

Video by Assad Tanoli from [Pexels](https://www.pexels.com/video/close-up-video-of-a-baby-5889561/)

# Set up
To facilitate its use, I have built a bash script called `setup.sh`. This will install python virtualenv to create a virtual environment where we will install everything we need. Check the file `requirements.txt` to know which python libraries we are using in the project.

To use it, simply type in your terminal

`bash setup.sh`

# Executing
You can run the `main.py` file as any other python file, but make sure to enable the virual environment by typing the command `source venv/bin/activate`. 

Also, you can use the bash script `run.sh`, which executes the `main.py` file using the virtual environment setup.

To use it, simply type in your terminal

`bash run.sh`

# Parameters
There are basically three parameters:
* ratio: It's the ratio of the output video
* th: It's a threshold parameter that controls the time coherence of the video. This threshold is used to control when the position of the detected face change a little bit. In other words, if the distance from current and previous position is larger than this threshold, the position is updated to the current one. However, if the such distance is smaller than the threshold, then it is kept in a history of positions, and the mean of the history is used as the final position. 
* filename: It's the filename of the video we want to process.

# Known issues
* There's a problem with the function Cropper.limitBoundaries(). It is not well defined and sometimes, it change the 
initial defined size of the frames. It implies that if we want to save the video using cv2.VideoWriter(), the video is not well written.
    I will solved asap.
