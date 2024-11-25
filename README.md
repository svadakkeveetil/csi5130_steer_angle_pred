# csi5130_steer_angle_pred
Steering wheel angle prediction for autonomous driving using image processing and neural networks

# Introduction

# Software requirements

- Pandas
- pygame
- ros package
- pip install tensorflow

# Running the video using ros

- Step 1 (ros directory): roscore
- Step 2 (ros directory) In a newtab: roslaunch ros_camera_playback mono_camera_cal.launch
- Step 3 (ros bag directory) In a newtab: rosbag play <bagfilename> --clock

# Running the extract images python file
- run roscore
- run roslaunch udacity_launch bag_launch
- run roslauhc udacity _launch rviz.launch
- run python script extract images
- run rosbag play bag file --clock



# Data Pre processing
HMB_1 - train_round2_part1.txt
round2/train/center/1479424215880976321.jpg
.
round2/train/center/1479424435919645985.jpg

HMB_2 - train_round2_part2.txt
round2/train/center/1479424439139199216.jpg
.
round2/train/center/1479425229026883882.jpg

HMB_4 - train_round2_part3.txt
round2/train/center/1479425729831388501.jpg
.
round2/train/center/1479425828498313000.jpg

HMB_5 - train_round2_part4.txt
round2/train/center/1479425834048269765.jpg
.
round2/train/center/1479426045784849999.jpg

HMB_6 - train_round2_part5.txt
round2/train/center/1479426202229245710.jpg
.
round2/train/center/1479426572343447996.jpg

# Evaluating Community Models
