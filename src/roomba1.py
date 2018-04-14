#!/usr/bin/env python

import rospy
import random
import math
import time

from geometry_msgs.msg import Twist

from math import sin
 
#Global stuff
msg = Twist()

def main():

    #topic differential drive is listening on
    pub = rospy.Publisher('roomba_control_1/cmd_vel', Twist, queue_size=10)

    #intializing the node
    rospy.init_node('roomba_control', anonymous=True)

    rate = rospy.Rate(10) 
    v = 0.333
    msg.linear.x = v
    msg.angular.z = 0
    time = rospy.get_rostime()
    
    ##TODO: figure out how units work in rospython and perfect the roomba behavior
    ##    : fix noise right after 180 rotation
    
    while not rospy.is_shutdown():
		## 180 degree turn every 20 seconds
		if (time.secs > 0 and time.secs % 20 == 0):
			stop = time.secs + 5.0
			while time.secs < stop:
				msg.linear.x = 0
				msg.angular.z= 1
				time = rospy.get_rostime()
				pub.publish(msg)
				rate.sleep()
		## 20 degree noise every 5 seconds
		elif (time.secs > 0 and time.secs % 5 == 0):
			t = random.uniform(-5,5)
			msg.angular.z = -1
			msg.linear.x = v
		## normal trajectory
		else:
			msg.angular.z = 0
			msg.linear.x = v	
			
		time = rospy.get_rostime()
		rospy.loginfo("Current time %i %i", time.secs, time.nsecs)
		pub.publish(msg)
		rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
