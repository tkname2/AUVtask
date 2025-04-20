#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(msg):
    print(msg.data)

if __name__=='__main__':
    rospy.init_node("chat_node",anonymous=True)
    
    username = input("Enter your name (Jolyne / Joestar): ")
    pub = rospy.Publisher('/chat_topic', String, queue_size=10)
    sub=rospy.Subscriber('/chat_topic', String, callback)
    rospy.loginfo("chat node has been started")
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        msg = input()
        full_msg = f"{username}: {msg}"
        pub.publish(full_msg)
        rate.sleep()
