import rclpy
from rclpy.node import Node
from task_one_interfaces.msg import TaskOne

class TaskOnePublisher(Node):
    def __init__(self, ang_vel, radius):
        super().__init__('Publisher')

        #creates a publisher that sends taskOne message on /taskone
        self.publisher = self.create_publisher(
            TaskOne,
            '/taskone',
            10
        )

        self.ang_vel = ang_vel
        self.radius = radius

        self.timer = self.create_timer(1.0, self.publish_data)

    def publish_data(self):
        msg = TaskOne()

        msg.ang_vel = self.ang_vel
        msg.radius = self.radius

        self.publisher.publish(msg)

        self.get_logger().info(
            f'Published: ang_vel = {msg.ang_vel}, radius = {msg.radius}\n'
        )

def main(args = None):
    print("--- Task One Publisher Configuration ---")
    
    try:
        user_ang_vel = float(input("Enter angular velocity (rad/s): "))
        user_radius = float(input("Enter wheel radius (m): "))
    except ValueError:
        print("Invalid input! Please enter number values next time./nUsing default values (5.0, 0.3)")
        user_ang_vel = 5.0
        user_radius = 0.3      

    rclpy.init(args = args)

    node = TaskOnePublisher(ang_vel = user_ang_vel, radius = user_radius)

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
        