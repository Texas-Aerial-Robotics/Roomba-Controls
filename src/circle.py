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
    
  
    while not rospy.is_shutdown():	
		if (time % 2 == 0):
			t = random.uniform(-.349,.349)
			msg.angular.z = t
			msg.linear.x = v
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
