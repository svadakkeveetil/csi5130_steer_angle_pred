import rospy
from dbw_mkz_msgs.msg import SteeringReport

def steering_report_callback(msg):
    rospy.loginfo(f"Steering Wheel Angle: {msg.steering_wheel_angle}")

def listener():
    rospy.init_node('steering_report_listener', anonymous=True)
    rospy.Subscriber('/vehicle/steering_report', SteeringReport, steering_report_callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
