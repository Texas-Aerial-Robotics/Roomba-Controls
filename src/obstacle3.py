#!/usr/bin/env python

import rospy
import math

from geometry_msgs.msg import Twist
from gazebo_msgs.msg import ContactsState
from math import sin

stop = 0

def callback(data):
    global stop
    rospy.loginfo(stop)
    #rospy.loginfo(len(data.states))
    if (len(data.states) != 0):
        stop = 1
        rospy.loginfo(stop)
    else:
        stop = 0

def main():
    global stop

    #topic differential drive is listening on
    pub = rospy.Publisher('obstacle_roomba_3/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber("front_bumper13", ContactsState, callback)

    #intializing the node
    rospy.init_node('roomba_control', anonymous=True)

    rate = rospy.Rate(10)
    msg = Twist()
    msg.linear.x = 0
    msg.angular.z = -.0666

    while not rospy.is_shutdown():
        if(stop == 1):
            msg.linear.x = 0
            msg.angular.z = 0

        else:
            msg.linear.x = .333
            msg.angular.z = -.0666

        pub.publish(msg)
        rate.sleep()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

