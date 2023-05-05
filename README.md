# yolo_detect_ros

# Installation and Setup
## Install forklift_pallt
```
mkdir forklift_pallet_det && cd forklift_pallet_det
git clone --recursive https://github.com/uptopia/forklift_pallet_det.git src
cd src/darknet_new
修改Makefile如下
make
cd ../..
catkin_make
```

## module
* Object Detection -- YOLOv4  
\* [YOLO_detect](/yolo_detect_ros/README.md)

## darknet_new Makefile說明
1. GPU                  是否開啟GPU
2. CUDNN,CUDNN_HALF     是否開啟cudnn加速(需安裝)
3. OPENCV               是否開啟opencv(需安裝)
4. OPENMP               是否開啟多核心CPU功能(視電腦是否支援)
5. LIBSO                開啟可獲得更多進階功能
建議：全部打開 0-> 1

## ERROR
/home/robotarm/forklift_pallet_ws/src/darknet_ros/darknet/src/parser.c:39:10: fatal error: version.h: No such file or directory
#include "version.h"
^~~~~~~~~~~
==> /home/robotarm/forklift_pallet_ws/src/darknet_ros/darknet/src/parser.c

LINE39 註解
LINE2011 PATCH_VERSION改成MAJOR_VERSION