#!/usr/bin/python

# Standard imports
import cv2
import numpy as np
import rospy
from visualization_msgs.msg import Marker


# Read image
#im = cv2.imread("/home/simon/ROB5/robopgave/robopgave_ws/src/robopgave_pkg/models/byu/textures/byu.jpg", cv2.IMREAD_COLOR)
im = cv2.imread("/home/simon/ROB5/robopgave/robopgave_ws/src/robopgave_pkg/models/byu/textures/byu.jpg", cv2.IMREAD_GRAYSCALE)
#im = cv2.imread("blob.jpg", cv2.IMREAD_GRAYSCALE)


# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 10
params.maxThreshold = 200


# filter by color
params.filterByColor = False
params.blobColor = 255


# Filter by Area.
params.filterByArea = True
params.minArea = 15

# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.9


# Filter by Convexity
params.filterByConvexity = False
params.minConvexity = 0.87

# Filter by Inertia
params.filterByInertia = False
params.minInertiaRatio = 0.1


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

im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (255, 0, 0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


for keypoint in keypoints:
    x = keypoint.pt[0]
    y = keypoint.pt[1]
    pose = [x, y]
    print(pose)
    # print(y)


# Show blobs
#cv2.imshow("Keypoints", im_with_keypoints)
#cv2.waitKey(0)


rospy.init_node("blobdetection")

marker_pub = rospy.Publisher("/visualization_marker", Marker, queue_size=2)

marker = Marker()

marker.header.frame_id = "/map"
marker.header.stamp = rospy.Time.now()

# set shape, Arrow: 0; Cube: 1 ; Sphere: 2 ; Cylinder: 3
marker.type = 2
marker.id = 0

# Set the scale of the marker
marker.scale.x = 1.0
marker.scale.y = 1.0
marker.scale.z = 1.0

# Set the color
marker.color.r = 0.0
marker.color.g = 1.0
marker.color.b = 0.0
marker.color.a = 1.0

# Set the pose of the marker
marker.pose.position.x = 0
marker.pose.position.y = 0
marker.pose.position.z = 0
marker.pose.orientation.x = 0.0
marker.pose.orientation.y = 0.0
marker.pose.orientation.z = 0.0
marker.pose.orientation.w = 1.0

marker_pub.publish(marker)

while not rospy.is_shutdown():
   
    rospy.rostime.wallsleep(1.0)
