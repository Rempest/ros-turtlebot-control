import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
class Control(Node):
    def __init__(self):
        super().__init__('Tutrle')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 15)
        self.timer = self.create_timer(0.5, self.motion)
    def motion(self):
        msg = Twist()
        msg.linear.x = 0.2
        msg.angular.z = 0.0
        self.publisher.publish(msg)
def main():
        rclpy.init(args = None)
        Turtle_Bot = Control()
        rclpy.spin(Turtle_Bot)
        Turtle_Bot.destroy_node()
        rclpy.shutdown()
if __name__ == '__main__':
       main()
        
        
        
        
        

