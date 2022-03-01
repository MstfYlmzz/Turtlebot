#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import threading

rospy.init_node("vel_pub",anonymous=True)

vel = Twist()
vel.linear.x = 0
vel.angular.z = 0
rospy.sleep(1)

for id in range(3):
    pub = rospy.Publisher("/tb3_{}/cmd_vel".format(id),Twist,queue_size=1)
    for i in range(10):
        pub.publish(vel)
        rospy.sleep(0.1)
    print("turtlebot {} is ready".format(id))

    
def publ(id):
    pub = rospy.Publisher("/tb3_{}/cmd_vel".format(id),Twist,queue_size=1)
    vel = Twist()
    vel.linear.x = 0.2
    vel.angular.z = 0.2
    pub.publish(vel)

if __name__ == "__main__":
    
    r = rospy.Rate(0.5)
    r.sleep()
    
    t0 = threading.Thread(target= publ, args= (0,))
    t1 = threading.Thread(target= publ, args = (1,))
    t2 = threading.Thread(target= publ, args = (2,))

    t0.start()
    t1.start()   
    t2.start()    


    
   
   
    