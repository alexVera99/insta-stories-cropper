#!/bin/bash

input_video='../videos/3.mp4'
output_audio='../videos/output/3.aac'

ffmpeg -i $input_video -vn -acodec copy $output_audio