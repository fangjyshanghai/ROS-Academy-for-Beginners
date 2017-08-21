#!/usr/bin/env python
# coding: utf-8
# filename: keyboard_photo_client2.py

import sys
import rospy
from simple_arm.srv import *

def keyboard_photo_client():

    rospy.init_node("take_photo_client")
    rospy.wait_for_service('take_photo')
    take_photo_client = rospy.ServiceProxy('take_photo',TakePhotoCommand)
    
    while not rospy.is_shutdown():
        try:
            command = raw_input('Please input command:')
            resp = take_photo_client(command)
            print resp.feedback
        except rospy.ServiceException, e:
            print "Service call failed: %s"%e

if __name__ == "__main__":
    keyboard_photo_client()
