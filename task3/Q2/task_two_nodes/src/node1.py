#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from task_two_interfaces.msg import RT2String

class Node1(Node):
    def __init__(self):
        super().__init__('node1')

        self.publisher = self.create_publisher(
            RT2String,
            '/input_string',
            10
        )

        self.user_input = input("Enter a string: ")
        self.timer = self.create_timer(1.0, self.publish_string)
    
    def publish_string(self):
        msg = RT2String()
        msg.data = self.user_input

        self.publisher.publish(msg)

        self.get_logger().info(
            f'Published: {self.user_input}'
        )

def main(args = None):
    rclpy.init(args = args)

    node = Node1()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()        
