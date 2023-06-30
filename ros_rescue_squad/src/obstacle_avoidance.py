#! /usr/bin/env python3

import rospy
import tf
import time
import actionlib

#from geomtry_msgs.msg import Twist
from nav_msgs.msg import OccupancyGrid

from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseResult, MoveBaseFeedback

# definition of the feedback callback. This will be called when feedback
# is received from the action server
# it just prints a message indicating a new message has been received

def feedback_callback(feedback):
    
    print('[Feedback] Going to Goal Pose...')

# initialiwes the action client node
rospy.init_node('move_base_action_client')

# create the connection to the action server
client = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
# wait for client
client.wait_for_server()
#goal 1 position
goal1 = MoveBaseGoal() 
goal1.target_pose.header.frame_id = 'map'
goal1.target_pose.pose.position.x = 0.8890800476074219
goal1.target_pose.pose.position.y = -0.42896175384521484
goal1.target_pose.pose.orientation.w = 1

#goal 2 position
goal2 = MoveBaseGoal()
goal2.target_pose.header.frame_id = 'map'
goal2.target_pose.pose.position.x = 2.484018325805664
goal2.target_pose.pose.position.y = -3.796830177307129
goal2.target_pose.pose.orientation.w = 1

#goal 3 position
goal3 = MoveBaseGoal()
goal3.target_pose.header.frame_id = 'map'
goal3.target_pose.pose.position.x = 7.09460973739624
goal3.target_pose.pose.position.y = -8.4793701171875
goal3.target_pose.pose.orientation.w = 1

#goal 4 position
goal4 = MoveBaseGoal()
goal4.target_pose.header.frame_id = 'map'
goal4.target_pose.pose.position.x = 7.425062656402588
goal4.target_pose.pose.position.y = -6.475271224975586
goal4.target_pose.pose.orientation.w = 1

#goal 5 position
goal5 = MoveBaseGoal()
goal5.target_pose.header.frame_id = 'map'
goal5.target_pose.pose.position.x = 8.015108108520508
goal5.target_pose.pose.position.y = -0.09460163116455078
goal5.target_pose.pose.orientation.w =  1

#goal 6 position
goal6 = MoveBaseGoal()
goal6.target_pose.header.frame_id = 'map'
goal6.target_pose.pose.position.x = 3.9580249786376953
goal6.target_pose.pose.position.y = -1.3102836608886719
goal6.target_pose.pose.orientation.w = 1

#goal 7 position
goal7 = MoveBaseGoal()
goal7.target_pose.header.frame_id = 'map'
goal7.target_pose.pose.position.x = 3.239400863647461
goal7.target_pose.pose.position.y = 2.8854551315307617
goal7.target_pose.pose.orientation.w = 1

#goal 8 position
goal8 = MoveBaseGoal()
goal8.target_pose.header.frame_id = 'map'
goal8.target_pose.pose.position.x = -1.1428146362304688
goal8.target_pose.pose.position.y = 5.171970367431641
goal8.target_pose.pose.orientation.w = 1

#goal 9 position
goal9 = MoveBaseGoal()
goal9.target_pose.header.frame_id = 'map'
goal9.target_pose.pose.position.x = -7.562620162963867
goal9.target_pose.pose.position.y = 0.7124395370483398
goal9.target_pose.pose.orientation.w = 1

#goal 10 position
goal10 = MoveBaseGoal()
goal10.target_pose.header.frame_id = 'map'
goal10.target_pose.pose.position.x = -4.765353202819824
goal10.target_pose.pose.position.y = -0.7522401809692383
goal10.target_pose.pose.orientation.w = 1

#goal 11 position
goal11 = MoveBaseGoal()
goal11.target_pose.header.frame_id = 'map'
goal11.target_pose.pose.position.x = -9.425585746765137
goal11.target_pose.pose.position.y = -3.212949752807617
goal11.target_pose.pose.orientation.w = 1

#goal 12 position

goal12 = MoveBaseGoal()
goal12.target_pose.header.frame_id = 'map'
goal12.target_pose.pose.position.x = -5.616065979003906
goal12.target_pose.pose.position.y = -7.218510627746582

goal12.target_pose.pose.orientation.w = 1
#goal 13 position
goal13 = MoveBaseGoal()
goal13.target_pose.header.frame_id = 'map'
goal13.target_pose.pose.position.x = -9.425585746765137
goal13.target_pose.pose.position.y = -3.212949752807617
goal13.target_pose.pose.orientation.w = 1

#goal 14 position
goal14 = MoveBaseGoal()
goal14.target_pose.header.frame_id = 'map'
goal14.target_pose.pose.position.x = -1.5513591766357422
goal14.target_pose.pose.position.y = 1.0052595138549805
goal14.target_pose.pose.orientation.w = 1






while not rospy.is_shutdown():
    # establishes a goal for the action server
    # Sends the objective to the action server with the feedback function specified to call when feedback received
    client.send_goal(goal1, feedback_cb=feedback_callback)
    client.wait_for_result()
    print('[Result] State: %d'%(client.get_state()))
    client.send_goal(goal2, feedback_cb=feedback_callback)
    client.wait_for_result()
    print('[Result] State: %d'%(client.get_state()))
    client.send_goal(goal3, feedback_cb=feedback_callback)
    client.wait_for_result()
    print('[Result] State: %d'%(client.get_state()))
    client.send_goal(goal4, feedback_cb=feedback_callback)
    client.wait_for_result()
    print('[Result] State: %d'%(client.get_state()))
    client.send_goal(goal5, feedback_cb=feedback_callback)
    client.wait_for_result()
    print('[Result] State: %d'%(client.get_state()))
    client.send_goal(goal6, feedback_cb=feedback_callback)
    client.wait_for_result()
    print('[Result] State: %d'%(client.get_state()))
    client.send_goal(goal7, feedback_cb=feedback_callback)
    client.wait_for_result()
    print('[Result] State: %d'%(client.get_state()))
    client.send_goal(goal8, feedback_cb=feedback_callback)
    client.wait_for_result()
    print('[Result] State: %d'%(client.get_state()))
    client.send_goal(goal9, feedback_cb=feedback_callback)
    client.wait_for_result()
    print('[Result] State: %d'%(client.get_state()))
    client.send_goal(goal10, feedback_cb=feedback_callback)
    client.wait_for_result()
    print('[Result] State: %d'%(client.get_state()))
    client.send_goal(goal11, feedback_cb=feedback_callback)
    client.wait_for_result()
    print('[Result] State: %d'%(client.get_state()))
    client.send_goal(goal12, feedback_cb=feedback_callback)
    client.wait_for_result()
    print('[Result] State: %d'%(client.get_state()))
    client.send_goal(goal13, feedback_cb=feedback_callback)
    client.wait_for_result()
    print('[Result] State: %d'%(client.get_state()))
    client.send_goal(goal14, feedback_cb=feedback_callback)
    client.wait_for_result()
    print('[Result] State: %d'%(client.get_state()))
  
  
  
  
  
  
  
    
