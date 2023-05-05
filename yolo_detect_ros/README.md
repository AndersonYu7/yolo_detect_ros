# Object Detection -- YOLOv4

## Real-Time Image Recognition
```
<terminal>
. devel/setup.bash
roslaunch yolo_detect_ros yolo_detect_altek_cam.launch
```

## Image Detection 
```
cd src/yolo_detect_ros/python

python3 image_detect.py [model_num] [data_path] [cfg_path] [weight_path] [data_path2] [cfg_path2] [weight_path2] .... [img_files_path]
```

## Video Detection
```
cd src/yolo_detect_ros/python

python3 video_detect.py [model_num] [data_path] [cfg_path] [weight_path] [data_path2] [cfg_path2] [weight_path2] .... [video_path]
```