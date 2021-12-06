#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist, Pose

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'Pose is %s', data.data) 

def move():
    # Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    pose_subscriber = rospy.Subscriber("/turtle1/pose", Pose, callback)
    vel_msg = Twist()

    def callback2(data):
        print("hello")

    pose_subscriber.callback = callback2
    #Receiveing the user's input
    print("Let's move your robot")
    speed = input("Input your speed:")
    destination = input("Type your coordinate: x, y").split(", ")
    


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

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass