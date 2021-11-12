#!/usr/bin/env python
import rospy
from std_msgs.msg import String

import cv2 as cv



def talker():
    pub = rospy.Publisher("chatter", String, queue_size=10)
    rospy.init_node("talker", anonymous=True)
    rate= rospy.Rate(10) #this means publish every 100th millisecond (10Hz)
    while not rospy.is_shutdown():
        hello_str = "THERE ARE MOMKEYS HERE %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
