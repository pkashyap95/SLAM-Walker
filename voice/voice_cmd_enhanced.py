#!/usr/bin/env python

"""
voice_cmd_vel.py is a simple demo of speech recognition.
  You can control a mobile base using commands found
  in the corpus file.
"""

import roslib; roslib.load_manifest('pocketsphinx')
import rospy
import math
import csv

from geometry_msgs.msg import Twist
from std_msgs.msg import String

class voice_cmd_vel:

    def __init__(self):
        rospy.on_shutdown(self.cleanup)
        self.speed = 0.2
        self.msg = Twist()

        # publish to cmd_vel, subscribe to speech output
        self.pub_ = rospy.Publisher('cmd_vel', Twist)
        rospy.Subscriber('recognizer/output', String, self.speechCb)
        r = rospy.Rate(10.0)
        while not rospy.is_shutdown():
            self.pub_.publish(self.msg)
            r.sleep()

    def create_marker(name, msg.linear.x, msg.linear.y):
		reader = csv.reader(open('coordinates.csv'))
		data = {}
		for row in reader:
		    key = row[0]
		    data[key] = row[1:]
		    
		print data

        coordinates = {'Name': name, 'x': msg.linear.x, 'y': msg.linear.y}
        for row in data:
            if name==row['name']
                    print("Location: ", name, " already exists")
                else:
                    data.append(coordinates)

        with open('coordinates.csv', 'wb') as csv_file:
    		writer = csv.writer(csv_file)
    		for key, value in data.items():
       			writer.writerow([key, value])

     # #Callback function implementing the pose value received
    # def callback(self, data):
    #     self.pose = data
    #     self.pose.x = round(self.pose.x, 4)
    #     self.pose.y = round(self.pose.y, 4)

    def get_distance(self, goal_x, goal_y):
        distance = sqrt(pow((goal_x - self.pose.x), 2) + pow((goal_y - self.pose.y), 2))
        return distance

    def move2goal(x, y):
        goal_pose = Pose()
        goal_pose.x = goal.x
        goal_pose.y = goal.y
        distance_tolerance = 0.5
        vel_msg = Twist()

        while sqrt(pow((goal_pose.x - self.pose.x), 2) + pow((goal_pose.y - self.pose.y), 2)) >= distance_tolerance:
            #Porportional Controller
            #linear velocity in the x-axis:
            vel_msg.linear.x = 1.5 * sqrt(pow((goal_pose.x - self.pose.x), 2) + pow((goal_pose.y - self.pose.y), 2))
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0

            #angular velocity in the z-axis:
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 4 * (atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x) - self.pose.theta)

            #Publishing our vel_msg
            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()
        #Stopping our robot after the movement is over
        vel_msg.linear.x = 0
        vel_msg.angular.z =0
        self.velocity_publisher.publish(vel_msg)
        rospy.spin()

    def where2move(msg.data):
        reader = csv.reader(open('coordinates.csv'))
		data = {}
		for row in reader:
		    key = row[0]
		    data[key] = row[1:]
		for row in data:
            if msg.data.find(data['name']) > -1:
                move2goal(row['x'], row['y'])
                break



    def speechCb(self, msg):
        rospy.loginfo(msg.data)

        if msg.data.find("full speed") > -1:
            if self.speed == 0.2:
                self.msg.linear.x = self.msg.linear.x*2
                self.msg.angular.z = self.msg.angular.z*2
                self.speed = 0.4
        if msg.data.find("half speed") > -1:
            if self.speed == 0.4:
                self.msg.linear.x = self.msg.linear.x/2
                self.msg.angular.z = self.msg.angular.z/2
                self.speed = 0.2

        if msg.data.find("forward") > -1:    
            self.msg.linear.x = self.speed
            self.msg.angular.z = 0
        elif msg.data.find("left") > -1:
            if self.msg.linear.x != 0:
                if self.msg.angular.z < self.speed:
                    self.msg.angular.z += 0.05
            else:        
                self.msg.angular.z = self.speed*2
        elif msg.data.find("right") > -1:    
            if self.msg.linear.x != 0:
                if self.msg.angular.z > -self.speed:
                    self.msg.angular.z -= 0.05
            else:        
                self.msg.angular.z = -self.speed*2
        elif msg.data.find("back") > -1:
            self.msg.linear.x = -self.speed
            self.msg.angular.z = 0
        elif msg.data.find("stop") > -1 or msg.data.find("halt") > -1:          
            self.msg = Twist()
        #creating marker at the specific location
        elif msg.data.find("THIS IS") > -1:
            create_marker(msg.data, msg.linear.x, msg.linear.y)

        elif msg.data.find("GO TO") > -1:
            where2move(msg.data)

        self.pub_.publish(self.msg)

    def cleanup(self):
        # stop the robot!
        twist = Twist()
        self.pub_.publish(twist)

if __name__=="__main__":
    rospy.init_node('voice_cmd_vel')
    try:
        voice_cmd_vel()
    except:
        pass
