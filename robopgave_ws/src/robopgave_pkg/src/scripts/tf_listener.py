import rospy
import tf2_ros
rospy.init_node("tf_listener")

tf_buffer = tf2_ros.Buffer()
listener = tf2_ros.TransformListener(tf_buffer)
rate = rospy.Rate(10.0)

while not rospy.is_shutdown():
    t = rospy.Time()
    try:
        map_odom_tf = tf_buffer.lookup_transform('map', 'odom', t)
        odom_base_tf = tf_buffer.lookup_transform('odom', 'base_footprint', t)
        print(odom_base_tf.transform.translation + odom_base_tf.transform.translation)

    except (tf2_ros.LookupException, tf2_ros.ConnectivityException,
            tf2_ros.ExtrapolationException):
        rate.sleep()
    continue
