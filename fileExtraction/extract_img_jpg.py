import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

# Initialize the ROS node
rospy.init_node('image_saver', anonymous=True)

# Create a CvBridge object to convert ROS image messages to OpenCV format
bridge = CvBridge()

# Callback function to process the image
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

# Subscribe to the image topic
image_topic = "/center_camera/image_color"  # Change this to your image topic
rospy.Subscriber(image_topic, Image, image_callback)

# Keep the node running
rospy.spin()
