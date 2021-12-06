#!/usr/bin/env python
from numpy.lib import twodim_base
import rospy
import numpy as np
import math
from geometry_msgs.msg import Twist
from rospy.topics import Publisher
from turtlesim.msg import Pose






def move():
    #Receiveing the user's input
    print("Let's move your robot")
    speed = int(input("Input your speed: "))
    vel_msg = Twist()
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    x, y = [ int(x) for x in input("Type your coordinateas x, y :").split(", ")]
    def callback(data):
        rospy.loginfo(rospy.get_caller_id() + 'Pose is %s', data.data) 

    def angular_pose_callback(data):
        angle = math.acos(x/math.sqrt(x**2 + y**2))
        if int(100*angle)/100 != int(100*data.theta)/100 :
            vel_msg.angular.z = 0.1*speed* np.sign(angle-data.theta)
            velocity_publisher.publish(vel_msg)
            rospy.loginfo(rospy.get_caller_id() + "Angule is %s", int(100*angle)/100)
            rospy.loginfo(rospy.get_caller_id() + "Theta is %s", int(100*data.theta)/100)
        else:
            vel_msg.angular.z = 0
            velocity_publisher.publish(vel_msg)
            linear_pose_callback(data)

    def linear_pose_callback(data):
        vel_msg.linear.x = speed
        velocity_publisher.publish(vel_msg)
        print("pront")

    rospy.init_node("Jens", anonymous=True)
    pose_subscriber = rospy.Subscriber("/turtle1/pose", Pose, angular_pose_callback)
    rospy.spin()
    

"""
    while not rospy.is_shutdown():

        #Setting the current time for distance calculus
        t0 = rospy.Time.now().to_sec()
        current_distance = 0
    
        #Loop to move the turtle in an specified distance
        while(current_distance < distance):
            #Publish the velocity
            velocity_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
            t1=rospy.Time.now().to_sec()
            #Calculates distancePoseStamped
            current_distance= speed*(t1-t0)
        #After the loop, stops the robot
        vel_msg.linear.x = 0
        #Force the robot to stop
        velocity_publisher.publish(vel_msg)
"""
if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass