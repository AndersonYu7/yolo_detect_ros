# yolo_detect_ros

# Installation and Setup
## Install forklift_pallt
```
mkdir [OWN_WORKSPACE] && cd [OWN_WORKSPACE]
git clone --recursive https://github.com/uptopia/forklift_pallet_det.git src
cd src/darknet_new
```
修改Makefile如下[Makefile說明](README.md#darknet_new-makefile說明)
```
make
cd ../..
catkin_make
```
## Setup
`cd src/yolo_detect_ros/yolo_network_config`

修改.data的names路徑(pallet_front.data and pallet_hole.data)
* /home/anderson/yolo_detect_ws/src/yolo_detect_ros/yolo_network_config/cfg/pallet_front.names

更改為
[WORKSAPCE_PATH]/src/yolo_detect_ros/yolo_network_config/cfg/pallet_front.names

* /home/anderson/yolo_detect_ws/src/yolo_detect_ros/yolo_network_config/cfg/pallet_hole.names

更改為
[WORKSAPCE_PATH]/src/yolo_detect_ros/yolo_network_config/cfg/pallet_hole.names


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

![Screenshot from 2023-05-05 19-34-30](https://user-images.githubusercontent.com/95768254/236451395-3d5e277c-bc53-4ba2-a0b6-624060e5ebd9.png)

## 載入模型
將.data .cfg .names 放入yolo_network_config/cfg中
修改.data的names路徑為[WORKSAPCE_PATH]/src/yolo_detect_ros/yolo_network_config/cfg/[names_file].names

將.weight放入yolo_network_config/weights中

修改config/pallet.yaml

將data_file cfg_file weight_file 依序改成自己模型的檔案

## yaml說明
![Screenshot from 2023-05-05 20-43-24](https://user-images.githubusercontent.com/95768254/236460660-cf34877b-61c0-4de2-853f-0b4063771162.png)

* data_file, config_file, weights_file 放模型data, cfg, weights的檔案（名稱＋副檔名即可）
* threshold 為預測閾值 只可偵測到數值大於設定的值
* model_num 為有多少個模型 ex:front+hole兩個模型 -> value = 2


## ERROR
/home/robotarm/forklift_pallet_ws/src/darknet_ros/darknet/src/parser.c:39:10: fatal error: version.h: No such file or directory
#include "version.h"
^~~~~~~~~~~
==> [WORKSPACE]/src/darknet_ros/darknet_new/src/parser.c

LINE39 註解
LINE2011 PATCH_VERSION改成MAJOR_VERSION
