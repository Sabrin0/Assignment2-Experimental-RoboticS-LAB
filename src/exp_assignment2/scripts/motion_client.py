#! /usr/bin/env python
from __future__ import print_function
import rospy

# Brings in the SimpleActionClient
import actionlib

# Brings in the messages used by the action, including the
# goal message and the result message.
from exp_assignment2.msg import *
from geometry_msgs.msg import Twist, Point, Pose
from nav_msgs.msg import Odometry

def motion_client():
    # Creates the SimpleActionClient, passing the type of the action
    # (FibonacciAction) to the constructor.
    client = actionlib.SimpleActionClient('/robot/reaching_goal_robot', exp_assignment2.msg.PlanningAction)

    # Waits until the action server has started up and started
    # listening for goals.
    client.wait_for_server()

    # Creates a goal to send to the action server.
    goal = exp_assignment2.msg.PlanningGoal()
    goal.target_pose_robot.pose.position.x = 0
    goal.target_pose_robot.pose.position.y = 0

    # Sends the goal to the action server.
    client.send_goal(goal)

    # Waits for the server to finish performing the action.
    client.wait_for_result()

    # Prints out the result of executing the action
    return client.get_result()  # A FibonacciResult
    
#pos_x = -3
#pos_y = -3

#rospy.init_node('motion_client')
#client = actionlib.SimpleActionClient('/reaching_goal_robot', exp_assignment2.msg.PlanningAction)
#client.wait_for_server()

#goal = exp_assignment2.msg.PlanningGoal()
#goal.target_pose.pose.position.x = pos_x
#goal.target_pose.pose.position.y = pos_y 

#client.send_goal(goal)
#client.wait_for_result()
#return client.get_result()

if __name__ == '__main__':
    try:
        # Initializes a rospy node so that the SimpleActionClient can
        # publish and subscribe over ROS.
        rospy.init_node('motion_client')
        result = motion_client()
        #print("Result:", ', '.join([str(n) for n in result.sequence]))
    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)
