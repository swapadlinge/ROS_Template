#!/usr/bin/env python3
import rclpy
from rclpy.node import Node 
from std_msgs.msg import Int64

class NumberCounterNode(Node): 
    def __init__(self):
        super().__init__("number_counter")
        self.number_ = 0  
        self.subscriber_ = self.create_subscription(Int64, "number", self.callback_number, 10)
        self.publisher_ = self.create_publisher(Int64, "number_count", 10)
        self.get_logger().info("Smartphone has been Started ..")

    def callback_number(self, msg):
        self.get_logger().info(str(msg.data))
        self.number_ += msg.data
        self.publish_count()

    def publish_count(self):
        msg = Int64()
        msg.data = self.number_
        self.publisher_.publish(msg)

def main(args = None):
    rclpy.init(args=args)
    node = NumberCounterNode()  
    
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()