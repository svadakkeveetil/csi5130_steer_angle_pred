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
t_start = 1479424439147
count = 0
# Callback function to process the image
def image_callback(msg):
    global image_time_stamp
    try:
        # Convert the ROS Image message to an OpenCV format (BGR)
        cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        # Save the image as a .jpg file
        image_time_stamp = int(rospy.get_time()*1e9)
        file_name = '/home/svadakkeveetil/AI_Project_Data/HMB_2/' + str(image_time_stamp) + '.jpg'
        cv2.imwrite(file_name, cv_image)
        rospy.loginfo(f"Image saved as {file_name}")
    except Exception as e:
        rospy.logerr(f"Error converting image: {e}")
# Subscribe to the image topic
#csvfile = open('train_round2_part1' + '.csv', 'w', newline='')
#writer = csv.writer(csvfile)
#writer.writerow(['timestamp','filename','angle','torque','speed','fullpath','filename2'])
image_topic = "/center_camera/image_color"  # Change this to your image topic
#steering_report_node = '/vehicle/steering_report'  # Get the steering wheel angle report
rospy.Subscriber(image_topic, Image, image_callback)
#rospy.Subscriber(steering_report_node, SteeringReport, extract_steering_angle)
#wait_for_all_subscriptions()
# Keep the node running
rospy.spin()