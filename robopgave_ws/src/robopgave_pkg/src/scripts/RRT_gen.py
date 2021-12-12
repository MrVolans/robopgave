import rospy
import geometry_msgs.msg as ge
from geometry_msgs.msg import PoseWithCovarianceStamped
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
import tf2_ros
from visualization_msgs.msg import Marker

DIST_EPSILON = 1.


def laser_callback(msg):
    for f in msg.ranges:
        if (f < DIST_EPSILON):
            #print("We're near a wall, " + str(f))
            return


def callback(msg):
    msg.pose.pose
    print(msg.pose.pose)



rospy.init_node('pose_listener')

tf_buffer = tf2_ros.Buffer()
listener = tf2_ros.TransformListener(tf_buffer)     
marker_pub = rospy.Publisher('/visualization_marker',Marker, queue_size=10)
t = rospy.Time()
rate = rospy.Rate(5.0)
odom_base_tf = tf2_ros.TransformStamped
while True:
    try:

        robot = Marker()
        robot.header.frame_id="map"
        robot.header.stamp=rospy.Time.now()
        # set shape, Arrow: 0; Cube: 1 ; Sphere: 2 ; Cylinder: 3
        robot.type = 2
        robot.id = 0
        robot.ns = "/yo"

        # Set the scale of the marker
        robot.scale.x = .2
        robot.scale.y = .2
        robot.scale.z = .2

        # Set the color
        robot.color.r = 2.0
        robot.color.g = 0.0
        robot.color.b = 0.0
        robot.color.a = 1.0

        # Set the pose of the marker
        robot.pose.position.x = 0
        robot.pose.position.y = 0
        robot.pose.position.z = 0
        robot.pose.orientation.x = 0.0
        robot.pose.orientation.y = 0.0
        robot.pose.orientation.z = 0.0
        robot.pose.orientation.w = 1.0

        #robot.pose.position = odom_base_tf.transform.translation


        marker_pub.publish(robot)
        #map_odom_tf = tf_buffer.lookup_transform('map', 'odom', t)
        ##pose = tf_buffer.canTransform(msg, "map")
        #odom_base_tf = tf_buffer.lookup_transform('map', 'base_footprint', rospy.Time())      
    except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException) as e:
        rate.sleep()
        print(e)
    continue



lidar_sub = rospy.Subscriber('/scan', LaserScan, laser_callback)
amcl_sub = rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped, callback)
rospy.spin()