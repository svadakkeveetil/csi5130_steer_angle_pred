import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import rosbag
import csv
from dbw_mkz_msgs.msg import SteeringReport
from std_msgs.msg import Float64

# Initialize the ROS node
rospy.init_node('image_and_steering_data_handler', anonymous=True)

# Create a CvBridge object to convert ROS image messages to OpenCV format
bridge = CvBridge()

# Callback function to process the image
def image_callback(msg):
    global image_time_stamp
    try:
        # Convert the ROS Image message to an OpenCV format (BGR)
        cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        
        # Save the image as a .png file
        image_time_stamp = int(rospy.get_time() * 1e3)
        file_name = '/home/svadakkeveetil/AI_Project_Data/HMB_1/' + str(image_time_stamp) + '.png'
        cv2.imwrite(file_name, cv_image)
        
        rospy.loginfo(f"Image saved as {file_name}")

    except Exception as e:
        rospy.logerr(f"Error converting image: {e}")

# Function to extract steering angle data from the rosbag and write it to a CSV file
def extract_steering_angle(bag_file, topic_name, fname, t_start):
    # Open the bag file
    with rosbag.Bag(bag_file, 'r') as bag:
        # Create a CSV file to store the extracted steering angle data
        with open(fname + '.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['time', 'steering_angle'])
            count = 1
            
            for topic, msg, t in bag.read_messages(topics=[topic_name]):
                t_temp = int((t.secs + t.nsecs / 1e9) * 1000)
                # Extract steering angle data and store it in the CSV file
                if t_temp > t_start and count <= 4401:
                    if isinstance(msg, SteeringReport):
                        steering_angle = msg.steering_wheel_angle
                        steering_angle_cmd = msg.steering_wheel_angle_cmd
                        writer.writerow([image_time_stamp, steering_angle])
                        rospy.loginfo(f"Timestamp: {t_temp}, Steering Wheel Angle: {steering_angle}, Steering Angle Command: {steering_angle_cmd}")
                        t_start += 50  # Adjust the starting time for each subsequent message
                        count += 1
                    else:
                        rospy.logwarn(f"Message type {msg._type} does not match the expected type!")
            rospy.loginfo(f"Extracted {count} steering angle records.")

if __name__ == "__main__":
    # Set parameters for the rosbag file and topic names
    bag_file = '/home/svadakkeveetil/AI_Project_Data/HMB_1.bag'  # Replace with your bag file path
    topic_name = '/vehicle/steering_report'  # Replace with the actual topic name
    bag_fname = '/home/svadakkeveetil/AI_Project_Data/HMB_1'  # Output CSV file path

    # Set the time for the first image
    t_start = 1479424215886  # Adjust to your starting time

    # Subscribe to the image topic to save images
    image_topic = "/center_camera/image_color"  # Change this to your image topic
    rospy.Subscriber(image_topic, Image, image_callback)

    # Call the function to extract steering angles from the rosbag and save to CSV
    extract_steering_angle(bag_file, topic_name, bag_fname, t_start)

    rospy.loginfo("Image saving and steering data extraction completed.")
    
    # Keep the node running while processing
    rospy.spin()
