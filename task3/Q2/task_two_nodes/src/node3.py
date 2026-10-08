#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, String

class Node3(Node):
    def __init__(self):
        super().__init__('node3')

        self.subscriber = self.create_subscription(
            Int32,
            '/palindrome_result',
            self.process_result,
            10
        )

        self.publisher = self.create_publisher(
            String,
            '/palindrome_response',
            10
        )

        self.get_logger().info('Node 3 started')
    
    def process_result(self, msg):
        response_msg = String()

        if msg.data == 1:
            response_msg.data = "Yes"
        else:
            response_msg.data = "No"    

        self.publisher.publish(response_msg)

        self.get_logger().info(
            f'Sent: {response_msg.data}'
        )

def main(args = None):
    rclpy.init(args = args)

    node = Node3()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()        
