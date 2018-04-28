#!/usr/bin/env python

import rospy
import random
import math
import time

from geometry_msgs.msg import Twist
from gazebo_msgs.msg import ContactsState


from math import sin
 
#Global stuff
msg = Twist()
flag_180 = 0

def callback(data):
	global flag_180
	rospy.loginfo(flag_180)
	#rospy.loginfo(len(data.states))
	if (len(data.states) != 0): 
	 	flag_180 = 1
	 	rospy.loginfo(flag_180)
	 	


def main():
    global flag_180
    #topic differential drive is listening on
    pub = rospy.Publisher('roomba_control_5/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber("front_bumper5", ContactsState, callback)

    #intializing the node
    rospy.init_node('roomba_control', anonymous=True)

    rate = rospy.Rate(10) 
    v = 0.333
    msg.linear.x = v
    msg.linear.z = 0
    current_angle = 0

    time = rospy.get_rostime()
    
    ##TODO:
    ##    : fix noise right after 180 rotation
    
    while not rospy.is_shutdown():
		## 180 degree turn every 20 seconds
		if (time.secs > 0 and time.secs % 20 == 0):
			initial_time = time.secs
			while (current_angle < math.pi):
				msg.linear.x = 0
   				msg.angular.z = math.pi/6
				flag_180 = 1
				time = rospy.get_rostime() 
				current_time = time.secs
				current_angle = (math.pi/6)*(current_time-initial_time)
				pub.publish(msg)
				rate.sleep()		
		## 20 degree noise every 5 seconds
		elif (time.secs > 0 and time.secs % 5 == 0 and flag_180 == 0):
			t = random.uniform(-.349,.349)
			msg.angular.z = t
			msg.linear.x = v

		elif (flag_180 == 1):
			initial_time = time.secs
			while (current_angle < math.pi):
				msg.linear.x = 0
   				msg.angular.z = math.pi/6
				flag_180 = 1
				time = rospy.get_rostime() 
				current_time = time.secs
				current_angle = (math.pi/6)*(current_time-initial_time)
				pub.publish(msg)
				rate.sleep()

		## normal trajectory
		else:
			msg.angular.z = 0
			msg.linear.x = v


		flag_180 = 0
		current_angle = 0
		time = rospy.get_rostime()
		pub.publish(msg)
		rate.sleep()
		


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

