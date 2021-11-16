#!/usr/bin/env python

import rospy
from robopgave_pkg.msg import Num
import cv2 as cv

def talker():
    pub = rospy.Publisher('chatter', Num, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        
        msg = Num("what is the answer?", "42")
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
