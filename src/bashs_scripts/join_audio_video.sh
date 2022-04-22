#!/bin/bash

input_video='../videos/output/output.avi'
input_audio='../videos/output/3.aac'
output_video='../videos/output/output_video_audio.mp4'

ffmpeg -i $input_video -i $input_audio -c:a copy $output_video