#!/usr/bin/python

# Standard imports
from logging import exception
from pickle import TRUE
import cv2
import numpy as np
import rospy
from visualization_msgs.msg import Marker


# Read image
#im = cv2.imread("/home/simon/ROB5/robopgave/robopgave_ws/src/robopgave_pkg/models/byu/textures/byu.jpg", cv2.IMREAD_COLOR)
im2 = cv2.imread("/home/polo/robopgave/robopgave_ws/src/robopgave_pkg/maps/map3.pgm", cv2.IMREAD_GRAYSCALE)
#im = cv2.imread("blob.jpg", cv2.IMREAD_GRAYSCALE)

im =cv2.flip(im2, 0)
w, h = im.shape
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

# Show blobs
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)
print("it runs")
rospy.init_node("goalpublisher")
marker_pub = rospy.Publisher("/visualization_marker", Marker, queue_size=2)
rate = rospy.Rate(5.0)
while not rospy.is_shutdown():
    try: 
        marker = Marker()
        marker.header.frame_id = "map"
        marker.header.stamp = rospy.Time.now()

        # set shape, Arrow: 0; Cube: 1 ; Sphere: 2 ; Cylinder: 3
        marker.type = 2
        marker.id = 0
        marker.ns = "/goals"
        # Set the scale of the marker
        marker.scale.x = .2
        marker.scale.y = .2
        marker.scale.z = .2

        # Set the color
        marker.color.r = 2.0
        marker.color.g = 0.0
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
        i=0

        for keypoint in keypoints :
            marker.id = i
            marker.pose.position.x = (keypoint.pt[0]-w/2-10)*0.05
            marker.pose.position.y = (keypoint.pt[1]-h/2-10)*0.05
            print(marker.pose.position)
            marker_pub.publish(marker)
            i=i+1
        marker_pub.publish(marker)
    except exception as e:
            rate.sleep()
            print("got an error")
            print(e)



