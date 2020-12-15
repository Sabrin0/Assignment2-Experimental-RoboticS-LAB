#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
import math
import time

rospy.init_node('head_ctrl', anonymous = True)

pub = rospy.Publisher('/robot/joint_head_controller/command', Float64, queue_size=1)
rate = rospy.Rate(1)
ctrl_c = False
    
    
while not ctrl_c:
    ## Check the connection in ordet to be sure to publish
    connections = pub.get_num_connections()
    if connections > 0:    
        for i in [-math.pi/4, 0 , math.pi/4, 0]:
            position_head = i
            rospy.loginfo(position_head)
            pub.publish(position_head)
            time.sleep(3)
            ctrl_c = True
        else:
            ## If the connection is 0 sleep and restart the loop
            rate.sleep()

