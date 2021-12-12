import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
from sensor_msgs.msg import LaserScan
DIST_EPSILON = 1.
def laser_callback(msg) : 
    for f in msg.ranges :
        if(f < DIST_EPSILON) :
            #print("We're near a wall, " + str(f))
            return

def callback(msg) :
    msg.pose.pose
    print(msg.pose.pose)

rospy.init_node('pose_listener')
lidar_sub = rospy.Subscriber('/scan', LaserScan, laser_callback)
odom_sub = rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped, callback)
rospy.spin()