#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from task_two_interfaces.msg import RT2String
from std_msgs.msg import Int32, String

class Node2(Node):
    def __init__(self):
        super().__init__('node2')

        #receives string from node1
        self.string_subscriber = self.create_subscription(
            RT2String,
            '/input_string',
            self.check_palindrome,
            10
        )

        # sends 1 or 0 to node 3
        self.result_publisher = self.create_publisher(
            Int32,
            '/palindrome_result',
            10
        )

        #receives yes or no from node 3
        self.response_subscriber = self.create_subscription(
            String,
            '/palindrome_response',
            self.receive_response,
            10
        )

        self.get_logger().info('Node 2 started')
    
    def check_palindrome(self, msg):
        text = msg.data

        if text == text[::-1]:
            result = 1
        else:
            result = 0

        result_msg = Int32()
        result_msg.data = result

        self.result_publisher.publish(result_msg)

        self.get_logger().info(
            f'Input: {text} | palindrome: {result}'
        )        

    def receive_response(self, msg):
        
        self.get_logger().info(
            f'Final Answer: {msg.data}'
        )

def main(args = None):
    rclpy.init(args = args)

    node = Node2()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()        
