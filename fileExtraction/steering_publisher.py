from dbw_mkz_msgs.msg import SteeringReport

def callback():
    # Send data using the SteeringReport message
    msg = SteeringReport()
    msg.steering_wheel_angle = 15.0
    # Publish to the topic
    publisher.publish(msg)
