# Object Detection -- YOLOv4

## Real-Time Image Recognition
```
<terminal>
. devel/setup.bash
roslaunch yolo_detect_ros yolo_detect_altek_cam.launch
```

## Image Detection in folder
```
cd src/yolo_detect_ros/python

python3 image_detect.py [model_num] [data_path] [cfg_path] [weight_path] [data_path2] [cfg_path2] [weight_path2] .... [img_files_path]
```
<img src="https://user-images.githubusercontent.com/95768254/236456035-0e73b0a5-d71f-42f1-b5cb-b80b1ca1a7db.jpg" width="640" height="360">

## Video Detection
```
cd src/yolo_detect_ros/python

python3 video_detect.py [model_num] [data_path] [cfg_path] [weight_path] [data_path2] [cfg_path2] [weight_path2] .... [video_path]
```
![out](https://user-images.githubusercontent.com/95768254/236455854-7898c16c-e89b-4385-8ad0-f8dea7f10e03.gif)
