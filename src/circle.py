#!/usr/bin/env python

import rospy
import random
import math
import time

from geometry_msgs.msg import Twist

from math import sin

def main():

    #topic differential drive is lisetning on
    pub = rospy.Publisher('roomba_control/cmd_vel', Twist, queue_size=10)

    #intializing the node
    rospy.init_node('circler', anonymous=True)

    rate = rospy.Rate(2) # 10hz
    msg = Twist()
    v = 0.333
    msg.linear.x = v
    msg.angular.z = 0
    time = rospy.get_time()
    
    ##sim gets kind of funky as time goes on...
    ##
    ##TODO: figure out how units work in rospython and perfect the roomba behavior
    ##    : figure out how to load multiple roombas...might be done through world file?
    ##    : fix time issues
    
    while not rospy.is_shutdown():
		## 180 degree turn every 20 seconds
		## TODO: for some reason some intervals are skipped...WHY?
		if (time > 0 and time % 20 == 0):
			stop = time + 5
			while time < stop:
				msg.linear.x = 0
				msg.angular.z= 1
				time = rospy.get_time()
				pub.publish(msg)
				rate.sleep()
		## 20 degree noise every 5 seconds
		elif (time > 0 and time % 5 == 0):
			t = random.uniform(-1,1)
			msg.angular.z = t
			msg.linear.x = v
		## normal trajectory
		else:
			msg.angular.z = 0
			msg.linear.x = v
			
		time = rospy.get_time()
		pub.publish(msg)
		rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
