import rospy
import cv2
from sensor_msgs.msg import Image
from dbw_mkz_msgs.msg import SteeringReport
from cv_bridge import CvBridge
import csv

# Initialize the ROS node
# rospy.init_node('image_saver', anonymous=True)
rospy.init_node('image_and_steering_data_sync', anonymous=True)
# Create a CvBridge object to convert ROS image messages to OpenCV format
bridge = CvBridge()
global count
t_start = 1479424215886
count = 0
def extract_steering_angle(msg):
    global t_start
    global count
    # Log the incoming steering data (e.g., steering wheel angle)
    t = msg.header.stamp
    t_temp = int((t.secs + t.nsecs/1e9)*1000)
    steering_angle = msg.steering_wheel_angle
    steering_angle_cmd = msg.steering_wheel_angle_cmd
    if t_temp > t_start and count<=4400:
        rospy.loginfo(f"I am working {t}, {t_start}")
        writer.writerow([image_time_stamp, steering_angle])
        rospy.loginfo(f"Timestamp: {t}, Steering Wheel Angle: {steering_angle}, steering_angle_cmd: {steering_angle_cmd}")
        #rospy.loginfo(f"Steering Wheel Angle: {msg.steering_wheel_angle}")
        #rospy.loginfo(f"Steering Wheel Angle Command: {msg.steering_wheel_angle_cmd}")
        rospy.loginfo(f"Timestamp: {t}")
        t_start+=50
        count+=1
    else:
        rospy.logwarn(f"Message type {msg._type} does not match the expected type!")

# Callback function to process the image
def image_callback(msg):
    global image_time_stamp
    try:
        # Convert the ROS Image message to an OpenCV format (BGR)
        cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        # Save the image as a .jpg file
        image_time_stamp = int(rospy.get_time()*1e9)
        file_name = '/home/dhavan/AI_Project/Data/HMB_1/' + str(image_time_stamp) + '.png'
        cv2.imwrite(file_name, cv_image)
        rospy.loginfo(f"Image saved as {file_name}")
    except Exception as e:
        rospy.logerr(f"Error converting image: {e}")
# Subscribe to the image topic
csvfile = open('HMB_1' + '.csv', 'w', newline='')
writer = csv.writer(csvfile)
writer.writerow(['time', 'steering_angle'])
image_topic = "/center_camera/image_color"  # Change this to your image topic
steering_report_node = '/vehicle/steering_report'  # Get the steering wheel angle report
rospy.Subscriber(image_topic, Image, image_callback)
rospy.Subscriber(steering_report_node, SteeringReport, extract_steering_angle)
# Keep the node running
rospy.spin()
