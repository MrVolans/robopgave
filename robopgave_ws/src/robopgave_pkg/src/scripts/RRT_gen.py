import rospy
import geometry_msgs.msg as ge
from geometry_msgs.msg import PoseWithCovarianceStamped
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
import tf2_ros
from visualization_msgs.msg import Marker
import cv2
import numpy as np

DIST_EPSILON = 1.


def laser_callback(msg):
    for f in msg.ranges:
        if (f < DIST_EPSILON):
            #print("We're near a wall, " + str(f))
            return


def callback(msg):
    msg.pose.pose
    print(msg.pose.pose)


# Read image
im = cv2.imread(
    "/home/simon/ROB5/robopgave/robopgave_ws/src/robopgave_pkg/models/byu/textures/byu.jpg", cv2.IMREAD_GRAYSCALE)
# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 10
params.maxThreshold = 200

# Filter by Area.
params.filterByArea = True
params.minArea = 15

# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.9

# Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3:
    detector = cv2.SimpleBlobDetector(params)
else:
    detector = cv2.SimpleBlobDetector_create(params)


# Detect blobs.
keypoints = detector.detect(im)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
# the size of the circle corresponds to the size of blob

im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array(
    []), (255, 0, 0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


# Show blobs
#cv2.imshow("Keypoints", im_with_keypoints)
# cv2.waitKey(0)


for keypoint in keypoints:
    x = keypoint.pt[0]
    y = keypoint.pt[1]
    arr = [x, y]
    print(arr)
            

rospy.init_node('pose_listener')

tf_buffer = tf2_ros.Buffer()
listener = tf2_ros.TransformListener(tf_buffer)
marker_pub = rospy.Publisher('/visualization_marker', Marker, queue_size=10)
t = rospy.Time()
rate = rospy.Rate(10.0)
while not rospy.is_shutdown():
    try:
        #map_odom_tf = tf_buffer.lookup_transform('map', 'odom', t)
        ##pose = tf_buffer.canTransform(msg, "map")
        odom_base_tf = tf_buffer.lookup_transform(
            'map', 'base_footprint', rospy.Time())
        robot = Marker()
        robot.header.frame_id = "map"
        robot.header.stamp = rospy.Time.now()
        # set shape, Arrow: 0; Cube: 1 ; Sphere: 2 ; Cylinder: 3
        robot.type = 2
        robot.id = 0

        # Set the scale of the marker
        robot.scale.x = .1
        robot.scale.y = .1
        robot.scale.z = .1

        # Set the color
        robot.color.r = 0.0
        robot.color.g = 1.0
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

        robot.pose.position = odom_base_tf.transform.translation

        marker_pub.publish(robot)
    except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException,):
        rate.sleep()
        print("SOmehitngs FISHY")
    continue


lidar_sub = rospy.Subscriber('/scan', LaserScan, laser_callback)
amcl_sub = rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped, callback)
rospy.spin()
