import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
class Control(Node):

    def __init__(self):
        super().__init__('turtle_controller')

        self.publisher = self.create_publisher(
            Twist,
            '/cmd_vel',
            15
        )

        self.timer = self.create_timer(
            0.5,
            self.motion
        )

        self.get_logger().info('Turtle controller started')

    def motion(self):
        msg = Twist()

        msg.linear.x = 0.2
        msg.angular.z = 0.0

        self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    turtle_bot = Control()

    try:
        rclpy.spin(turtle_bot)
    except KeyboardInterrupt:
        pass
    finally:
        turtle_bot.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
        
        
        
        
        

