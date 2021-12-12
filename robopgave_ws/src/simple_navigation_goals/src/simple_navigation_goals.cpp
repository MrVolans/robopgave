#include <ros/ros.h>
#include "iostream"
#include <move_base_msgs/MoveBaseAction.h>
#include <actionlib/client/simple_action_client.h>
#include <geometry_msgs/Pose.h>
#include <math.h>
#include <list>
using namespace geometry_msgs;
typedef actionlib::SimpleActionClient<move_base_msgs::MoveBaseAction> MoveBaseClient;

void generateRRT(void *goal, void *pos)
{
  bool arrived;
  double new_length;
  while (arrived)
  {
    if (pos = goal)
    {
      return;
    }

    new_length = rand() % 20 + 1;
  }
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "simple_navigation_goals");

  //tell the action client that we want to spin a thread by default
  MoveBaseClient ac("move_base", true);

  //wait for the action server to come up
  while (!ac.waitForServer(ros::Duration(5.0)))
  {
    ROS_INFO("Waiting for the move_base action server to come up");
  }
  Point point1;
  point1.x = -2.54;
  point1.y = 2.619;

  Point point2;
  point2.x = 2.475;
  point2.y = 1.504;

  Point point3;
  point3.x = 2.69;
  point3.y = 2.93;

  Point point4;
  point4.x = 1.490;
  point4.y = -2.749;

  Point point5;
  point5.x = -2.653;
  point5.y = -2.379;

  Point point6;
  point6.x = -2.490;
  point6.y = 0.497;

  std::list<Point> points {point1, point2, point3, point4, point5, point6};
  move_base_msgs::MoveBaseGoal goal;

  for (Point g : points)
  {
    goal.target_pose.pose.position = g;
    //we'll send a goal to the robot to move 1 meter forward
    goal.target_pose.header.frame_id = "map";
    goal.target_pose.header.stamp = ros::Time::now();

    goal.target_pose.pose.orientation.w = 1;
    ROS_INFO("Sending goal");
    ac.sendGoal(goal);

    ac.waitForResult();

    if (ac.getState() == actionlib::SimpleClientGoalState::SUCCEEDED)
      ROS_INFO("Hooray, the base moved 1 meter forward");
    else
      ROS_INFO("The base failed to move forward 1 meter for some reason");
  }
  popen("rosrun map_server map_saver -f /home/polo/robopgave/robopgave_ws/src/robopgave_pkg/maps/map3 map:=map", "r");
  return 0;
}

/*
Pose(Point(-2.474, 2.619, 0.000), Quaternion(0.000, 0.000, 0.985, 0.174))
Pose(Point(2.475, 1.504, 0.000), Quaternion(0.000, 0.000, 0.021, 1.000))
Pose(Point(2.564, 3.002, 0.000), Quaternion(0.000, 0.000, 0.018, 1.000))
Pose(Point(1.490, -2.749, 0.000), Quaternion(0.000, 0.000, -0.999, 0.034))

Pose(Point(-2.653, -2.379, 0.00), Quaternion(0.000, 0.000, 0.999, 0.052))
Pose(Point(-2.490, 0.497, 0.000), Quaternion(0.000, 0.000, 0.654, 0.756))
*/