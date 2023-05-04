#!/usr/bin/env python3
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def usb_cam_publisher():
    cap = cv2.VideoCapture(0)
    bridge = CvBridge()
    pub = rospy.Publisher('usb_cam/image_raw', Image, queue_size=10)
    rospy.init_node('usb_cam_publisher', anonymous=True)
    rate = rospy.Rate(30) # 30hz
    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if not ret:
            rospy.logerr("Can't receive frame (stream end?). Exiting ...")
            break
        ros_img = bridge.cv2_to_imgmsg(frame, encoding="bgr8")
        pub.publish(ros_img)
        rate.sleep()

    cap.release()

if __name__ == '__main__':
    try:
        usb_cam_publisher()
    except rospy.ROSInterruptException:
        pass
