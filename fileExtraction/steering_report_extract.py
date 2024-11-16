import rosbag
from std_msgs.msg import Float64  # Or the appropriate message type
from dbw_mkz_msgs.msg import SteeringReport
import rospy
import csv

# Define the function to extract steering wheel data and write it in a csv_file
def extract_steering_angle(bag_file, topic_name, fname, t_start):
    # Open the bag file
    with rosbag.Bag(bag_file, 'r') as bag:
        # Iterate over the messages in the bag file for the specified topic
        csvfile = open(fname+'_stering.csv', 'w', newline='')
        csvfiler = open('HMB1.csv', 'r', newline='')
        writer = csv.writer(csvfile)
        r_file = csv.reader(csvfiler)
        r_data = list(r_file)
        writer.writerow(['time', 'steering_angle'])
        count = 0
        for topic, msg, t in bag.read_messages(topics=[topic_name]):
            t_temp = int((t.secs + t.nsecs/1e9)*1000)
            # Assuming the message is of type std_msgs/Float64
            if t_temp > t_start and count<=4400:
                print(type(msg.steering_wheel_angle))
                frame_id = msg.header.seq
                steering_angle = msg.steering_wheel_angle
                steering_angle_cmd = msg.steering_wheel_angle_cmd
                writer.writerow([r_data[count][0], steering_angle])
                rospy.loginfo(f"Frame_ids: {frame_id}, Timestamp: {t}, Steering Wheel Angle: {steering_angle}, steering_angle_cmd: {steering_angle_cmd}")
                t_start+=50
                count += 1
            else:
                rospy.logwarn(f"Message type {msg._type} does not match the expected type!")
        print(count)

if __name__ == "__main__":
    rospy.init_node('steering_angle_extractor', anonymous=True)

    bag_file = '/home/svadakkeveetil/AI_Project_Data/HMB_1.bag'  # Replace with your bag file path
    topic_name = '/vehicle/steering_report'  # Replace with the actual topic name
    bag_fname = 'HMB_1'

    # time for first image
    t_start = 1479424215886

    # Call the function to extract steering angles
    extract_steering_angle(bag_file, topic_name, bag_fname, t_start)
    print("Data stored in 'HMB_1.csv'")
