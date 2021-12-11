#!/usr/bin/env python
from numpy.lib import twodim_base
import rospy
import numpy as np
import math
from geometry_msgs.msg import Twist
from rospy.topics import Publisher
from turtlesim.msg import Pose

DISTANCE_EPSILON = 0.1
ANGLE_EPSILON = 0.01
position = np.array([0,0])
speeddiv = 0.15
xUnit = np.array([1, 0])

def move():
    #Receiveing the user's input
    print("Let's move your robot")
    speed = int(input("Input your speed: "))
    vel_msg = Twist()
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    destination = np.array([int(x) for x in input("Type your coordinateas x, y :").split(", ")])
    def callback(data):
        position = np.array([data.x, data.y])
        rospy.loginfo(rospy.get_caller_id() + 'Pose is %s', data.data) 
    
    def angular_pose_callback(data):

        distance = destination-position
        if np.linalg.norm(distance) < DISTANCE_EPSILON :
            print("Too short")
            return
        direction = distance/np.linalg.norm(distance)
        rotationAngle = math.acos(np.dot(xUnit, direction))+data.theta
        if abs(rotationAngle) > ANGLE_EPSILON:
            vel_msg.angular.z = np.sign(rotationAngle)*speed*speeddiv
            velocity_publisher.publish(vel_msg)
            rospy.loginfo(rospy.get_caller_id() + " Angule is %s", rotationAngle)
            rospy.loginfo(rospy.get_caller_id().split("_")[0] + " Theta is %s", int(100*data.theta)/100)
        else:
            vel_msg.angular.z = 0
            velocity_publisher.publish(vel_msg)
            linear_pose_callback(data)

    def linear_pose_callback(data):
        position = np.array([data.x, data.y])
        distance_To_Goal = np.linalg.norm(destination-position)
        rospy.loginfo(rospy.get_caller_id().split("_")[0] + " Distance is: %s", distance_To_Goal)
        if distance_To_Goal < 0.1 :
            vel_msg.linear.x = 0
            rospy.loginfo("arrived at %s", position)
        else :
            vel_msg.linear.x = speed/4
            velocity_publisher.publish(vel_msg)
        

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