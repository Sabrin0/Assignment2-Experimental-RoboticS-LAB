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
import math
import random
import sys
import rospy
import actionlib
from std_msgs.msg import String, Float64
from exp_assignment2.msg import *
from exp_assignment2.msg import BallState
from geometry_msgs.msg import Twist, Point, Pose
from nav_msgs.msg import Odometry

## Define home x position 
x_home = -6
## Define home y position 
y_home = 6

## Define person x position 
#x_person = 0
## Define person x position
#y_person = 0

## Initial state

BallDetected = False
BallCheck = False


client = actionlib.SimpleActionClient('/robot/reaching_goal_robot', exp_assignment2.msg.PlanningAction)

# Functions 
def decision():
    """! return random state between GoTonormal or GoToSleep"""
    return random.choice(['GoToNormal','GoToSleep'])

# Pub that moves head 

def head_control():

    pub_stop = rospy.Publisher("/robot/cmd_vel", Twist, queue_size=1)                                   
    pub_head = rospy.Publisher('/robot/joint_head_controller/command', Float64, queue_size=1)
    rate = rospy.Rate(1)
    ctrl_c = False
      
    while not ctrl_c:
        ## Check the connection in ordet to be sure to publish
        connections = pub_head.get_num_connections()
        if connections > 0:
            rospy.loginfo('wooof!')
            stop = Twist()
            stop.angular.z = 0
            stop.linear.x = 0
            pub_stop.publish(stop)
            
            for i in [-math.pi/4, 0 , math.pi/4, 0]:
                
                position_head = i
                #rospy.loginfo('looking around at %d',position_head)
                pub_head.publish(position_head)
                time.sleep(3)
                ctrl_c = True
            time.sleep(5)
        else:
            ## If the connection is 0 sleep and restart the loop
            rate.sleep()

def callback_check(data):

    """! Callback related to ball detection"""
    global BallDetected, BallCheck, currentRadius
    BallDetected = data.BallDetected
    currentRadius = data.currentRadius

    if (BallDetected == True) and (BallCheck == False):
        BallCheck = True
        rospy.loginfo("Ball Detected! Start tracking ")
        client.cancel_all_goals()


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
        self.rate = rospy.Rate(1) 
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

        global BallDetected
        
        self.counter = random.randint(1,2)
        goal = exp_assignment2.msg.PlanningGoal()

        while not rospy.is_shutdown():  
            #rospy.loginfo(rospy.get_caller_id() + 'Executing state NORMAL ')
            #time.sleep(1)
            if (BallDetected == True) and (BallCheck == True):
                #rospy.loginfo("passo da normale a play flag preso")
                return 'GoToPlay'
        
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
            #rospy.loginfo('Checking around...')
            #head_control()
            #print('Nothing interesting')
            time.sleep(2)
            self.rate.sleep()
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
        self.rate = rospy.Rate(200)  # Loop at 50 Hz
        
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
    def __init__(self):
        smach.State.__init__(self, 
                            outcomes=['GoToNormal','GoToPlay'])
        #rospy.loginfo('sar il rate')
        self.rate = rospy.Rate(200)  # Loop at 50 Hz
        #rospy.loginfo('prima del exec')

    def execute(self, userdata):

        rospy.loginfo("Executing state PLAY")

        global currentRadius, BallDetected, BallCheck
        while True:
            
            if (currentRadius > 90):
                #rospy.loginfo('muovo la testa')
                head_control()
            if (BallDetected == False):
                BallCheck = False
                rospy.loginfo('WOOF! Palla Persa :(')
                return 'GoToNormal'

            #print(currentRadius)
            #print(BallDetected)
            time.sleep(3)       
        

def main():
    
    rospy.init_node('smach_example_state_machine')
    ##Node subscibes to Ball State topic
    rospy.Subscriber('/robot/BallState', BallState, callback_check)
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