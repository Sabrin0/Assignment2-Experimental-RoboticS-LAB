#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
import math
import time

def head_control():
    pub = rospy.Publisher('/robot/joint_head_controller/command', Float64, queue_size=10)
    rospy.init_node('head_ctrl', anonymous = True)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        hello_str = "tempo %s" % rospy.get_time()
        
        for i in [-math.pi/4, 0 , math.pi/4, 0]:
            position_head = i
            rospy.loginfo(position_head)
            pub.publish(position_head)
            time.sleep(2)

if __name__ == '__main__':
    try:
        head_control()
    except rospy.ROSInterruptException:
        pass