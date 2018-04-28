#!/usr/bin/env python

import rospy
import math

from geometry_msgs.msg import Twist
from math import sin
 

def main():

    #topic differential drive is listening on
    pub = rospy.Publisher('obstacle_roomba_1/cmd_vel', Twist, queue_size=10)

    #intializing the node
    rospy.init_node('roomba_control', anonymous=True)

    rate = rospy.Rate(10)
    msg = Twist() 
    msg.linear.x = 0
    msg.angular.z = -.0666
    
    while not rospy.is_shutdown():
	msg.linear.x = .333 
	pub.publish(msg)
	rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

