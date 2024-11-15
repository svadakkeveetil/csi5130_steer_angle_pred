import rosbag
from std_msgs.msg import Float64  # Or the appropriate message type
from dbw_mkz_msgs.msg import SteeringReport
import rospy
import csv
# Required for storing the image
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
# Image extraction

def image_callback(msg):
    try:
        # Convert the ROS Image message to an OpenCV format (BGR)
        cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        
        # Save the image as a .jpg file
        file_name = '/home/svadakkeveetil/AI_Project_Data/HMB_1/' + str(int(rospy.get_time()*1e9)) + '.png'
        cv2.imwrite(file_name, cv_image)
        
        rospy.loginfo(f"Image saved as {file_name}")

    except Exception as e:
        rospy.logerr(f"Error converting image: {e}")
# Define the function to extract steering wheel data and write it in a csv_file
def extract_steering_angle(bag_file, topic_name, fname):
    # Open the bag file
    with rosbag.Bag(bag_file, 'r') as bag:
        # Iterate over the messages in the bag file for the specified topic
        csvfile = open(fname+'.csv', 'w', newline='')
        writer = csv.writer(csvfile)
        writer.writerow(['frame_id', 'steering_angle'])
        for topic, msg, t in bag.read_messages(topics=[topic_name]):
            # Assuming the message is of type std_msgs/Float64
            print(type(msg.steering_wheel_angle))
            if 1==1:
                steering_angle = msg.steering_wheel_angle
                steering_angle_cmd = msg.steering_wheel_angle_cmd
                writer.writerow([t, steering_angle])
                rospy.loginfo(f"Timestamp: {t}, Steering Wheel Angle: {steering_angle}, steering_angle_cmd: {steering_angle_cmd}")
                print('line written')
            else:
                rospy.logwarn(f"Message type {msg._type} does not match the expected type!")

if __name__ == "__main__":
    rospy.init_node('steering_angle_extractor', anonymous=True)

    bag_file = '/home/svadakkeveetil/AI_Project_Data/HMB_1.bag'  # Replace with your bag file path
    topic_name = '/vehicle/steering_report'  # Replace with the actual topic name
    bag_fname = 'HMB_1'

    # Call the function to extract steering angles
    extract_steering_angle(bag_file, topic_name, bag_fname)
    print("Data stored in 'HMB_1.csv'")