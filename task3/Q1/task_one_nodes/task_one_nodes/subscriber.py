import rclpy
from rclpy.node import Node
from task_one_interfaces.msg import TaskOne
class TaskOneSubscriber(Node):
    def __init__(self):
        super().__init__('Subscriber')

        self.subscription = self.create_subscription(
            TaskOne,
            '/taskone',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        speed = msg.ang_vel * msg.radius

        self.get_logger().info(
            f'Recieved: ang_vel = {msg.ang_vel}, radius = {msg.radius:.2f}'
        )

        self.get_logger().info(
            f'Longitudinal wheel speed = {speed:.2f} m/s\n'
        )

def main(args = None):
    rclpy.init(args = args)

    node = TaskOneSubscriber()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
