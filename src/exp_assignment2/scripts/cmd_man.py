#!/usr/bin/env python

"""!
@author Luca Covizzi
@mainpage Assignment 2 Exprob
@package cmd_man
@section Description
This script implements a ROS node that is a subscriber of get_pos and user_play publishers and at the same time it implements the FSM.
In this way, according to the command stored, it's possible to resarch the desired state.   
"""

from __future__ import print_function

# Imports
import roslib; roslib.load_manifest('exp_assignment2')
import rospy
import smach
import smach_ros
import time
import random
import sys
import rospy
import actionlib
from std_msgs.msg import String #Float64
from exp_assignment2.msg import *
from geometry_msgs.msg import Twist, Point, Pose
from nav_msgs.msg import Odometry

# Global Constants
## Initialize target x position
x_pos = 0
## Initialize target y position
y_pos = 0

## Define home x position 
x_home = -6
## Define home y position 
y_home = -6

## Define person x position 
x_person = 0
## Define person x position
y_person = 0

## Initial state
# state = 'NoInfo'

# Functions 
def decision():
    """! return random state between GoTonormal or GoToSleep"""
    return random.choice(['GoToNormal','GoToSleep'])



def callback_pos(data):
    """! Callback related to target position
    @param x_pos x positon of the robot
    @param y_pos y position of the robot
    """
#    global x_pos
#    x_pos = data.linear.x
#    global y_pos 
#    y_pos = data.linear.y

#def callback_user(data):
    """! Callback related to user command request 
    @param state string that actives the PLAY state
    """
#    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
#    global state
#    state = "play"

# define a client to call later in the normal and sleep behaviour 
client = actionlib.SimpleActionClient('/robot/reaching_goal_robot', exp_assignment2.msg.PlanningAction)

class Normal(smach.State):
    """! Define normal state """
    def __init__(self):
        """! initialisation function, it should not wait 
        @param outcomes outcomes of the state
        @param input_keys counter in
        @param output_keys counter out
        """
        smach.State.__init__(self, 
                             outcomes=['GoToNormal','GoToSleep','GoToPlay'])
                             #input_keys=['unlocked_counter_in'],
                             #output_keys=['unlocked_counter_out'])
        #self.rate = rospy.Rate(1) 
        self.counter = 0
    
    def execute(self,userdata):

        """! Normal state execution 
        @param x_pos x positon of the robot
        @param y_pos y position of the robot
        @return state researched
        """
        # time.sleep(3)
        # global x_pos
        # global y_pos
        # global state
        
        self.counter = random.randint(1,2)
        goal = exp_assignment2.msg.PlanningGoal()

        while not rospy.is_shutdown():  
            #rospy.loginfo(rospy.get_caller_id() + 'Executing state NORMAL ')
            #time.sleep(1)

            #if state == "play":
            #    state = 'noInput'
            #    return 'GoToPlay'

            if self.counter == 3:
                return 'GoToSleep'
            # Waits until the action server has started up and started listening for goals.             
            # client.wait_for_server()
            # Create a goal to send to the action server.
            
            goal.target_pose_robot.pose.position.x = random.randint(-6,6)
            goal.target_pose_robot.pose.position.y = random.randint(-6,6)
            rospy.loginfo('i m going to x: %d y: %d',goal.target_pose_robot.pose.position.x, goal.target_pose_robot.pose.position.y )
            client.send_goal(goal)           
            # Prints out the result of executing the action
            #return client.get_result()
            client.wait_for_result()
            rospy.loginfo('i m arrived')
            self.counter += 1

        return 'GoToSleep'

class Sleep(smach.State):
    """! Define Sleep state """
    def __init__(self):
        """! initialisation function, it should not wait 
        @param outcomes outcomes of the state
        @param input_keys counter in
        @param output_keys counter out
        """
        smach.State.__init__(self, 
                             outcomes=['GoToNormal','GoToSleep'])
                             #input_keys=['locked_counter_in'],
                             #output_keys=['locked_counter_out'])
        #self.sensor_input = 0
        self.rate = rospy.Rate(50)  # Loop at 50 Hz
        
    def execute(self, userdata):
        """! Sleep state execution 
        @param x_home x positon of the home
        @param y_home y position of the home
        @return state Normal
        """
        #time.sleep(5)
        global x_home
        global y_home

        rospy.loginfo(rospy.get_caller_id() + 'Executing state SLEEP ')
        goal = exp_assignment2.msg.PlanningGoal()
        goal.target_pose_robot.pose.position.x = x_home
        goal.target_pose_robot.pose.position.y = y_home
        rospy.loginfo(rospy.get_caller_id() + 'Back home x: %d y: %d',x_home,y_home)
        client.send_goal(goal)           
        # Prints out the result of executing the action
        #return client.get_result()
        client.wait_for_result()
        rospy.loginfo('i m arrived, now i will take a nap')
        time.sleep(3)
        self.rate.sleep()
        return 'GoToNormal'

class Play(smach.State):
    """! Define Play state """
    def __init__(self):
        """! initialisation function, it should not wait 
        @param outcomes outcomes of the state
        @param input_keys counter in
        @param output_keys counter out
        """
        smach.State.__init__(self, 
                             outcomes=['GoToNormal','GoToPlay'])
                             #input_keys=['locked_counter_in'],
                             #output_keys=['locked_counter_out'])
        
        self.rate = rospy.Rate(50)  # Loop at 50 Hz

    def execute(self, userdata):
         """! Play state execution 
        @param x_pos x positon of the robot
        @param y_pos y position of the robot
        @param x_home y position of home
        @param y_home y position of home
        @return GoToNormal state
        """
        #global x_pos
        #global y_pos 

        #nav_client(x_pos,y_pos)
        #nav_client(x_person,y_person)

        #rospy.loginfo(' Executing state PLAY ')
        #time.sleep(3)

        #return 'GoToNormal'       


def main():
    
    rospy.init_node('smach_example_state_machine')
    client.wait_for_server()

    ## Node subscribes to chatter topic
    ## rospy.Subscriber('chatter', String, callback_user)
    ## Node subscribes to position_xy topic
    ## rospy.Subscriber('position_xy', Twist, callback_pos)
    
    ## Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['container_interface'])
    sm.userdata.sm_counter = 0

    ## Open the container
    with sm:
        # Add states to the container
        smach.StateMachine.add('NORMAL', Normal(), 
                               transitions={'GoToSleep':'SLEEP', 
                                            'GoToNormal':'NORMAL',
                                            'GoToPlay':'PLAY'})
                               #remapping={'locked_counter_in':'sm_counter', 
                                          #'locked_counter_out':'sm_counter'})
        smach.StateMachine.add('SLEEP', Sleep(), 
                               transitions={'GoToSleep':'SLEEP', 
                                            'GoToNormal':'NORMAL'})
                               #remapping={'unlocked_counter_in':'sm_counter',
                                          #'unlocked_counter_out':'sm_counter'})
        smach.StateMachine.add('PLAY', Play(),
                                transitions={'GoToNormal':'NORMAL',
                                             'GoToPlay':'PLAY'})
                                #remapping={'unlocked_counter_in':'sm_counter',
                                           #'unlocked_counter_out':'sm_counter'})

    # Create and start the introspection server for visualization
    sis = smach_ros.IntrospectionServer('server_name', sm, '/SM_ROOT')
    sis.start()

    # Execute the state machine
    outcome = sm.execute()

    # Wait for ctrl-c to stop the application
    rospy.spin()
    sis.stop()


if __name__ == '__main__':
    main()