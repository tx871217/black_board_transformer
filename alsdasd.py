#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
import time
import math

goal_pos = {
    "x": -50,
    "y": 0
}


def distance(msg):
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    dis = math.sqrt((goal_pos["x"] - x)**2 + (goal_pos["y"] - y)**2)
    return dis

def callback(msg):
    dis = distance(msg)
    if dis < 1 :
        print("Arriveed!!!")
    else:
        print(dis)

rospy.init_node('check_odometry')
odom_sub = rospy.Subscriber('/odom', Odometry, callback)
rospy.spin()