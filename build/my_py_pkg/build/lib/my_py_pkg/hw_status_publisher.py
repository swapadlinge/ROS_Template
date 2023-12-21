#!/usr/bin/env python3
import rclpy
from rclpy.node import Node 
from my_robot_interfaces.msg import HardwareStatus


class HardwareStatusPublisherNode(Node): 
    def __init__(self):
        super().__init__("hardware_status_publisher")   
        self.hardware_status_publisher_ = self.create_publisher("hardware_status",10)
        self.timer_= self.create_timer(1.0,self.hardware_status_publisher)
        self.get_logger().info("Hardware status publisher has been started ....")

    def publish_hw_status(self):
        msg = HardwareStatus()
        msg.temprature = 45
        msg.are_motors_ready = True
        msg.message = "Nothig special Here"
        self.hardware_status_publisher_.publish(msg)
   

def main(args = None):
    rclpy.init(args=args)
    node = HardwareStatusPublisherNode()  
    
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()