import rclpy
from rclpy.node import Node
from std_msgs.msg import String
class Empty(Node):
    def __init__(self):
       super().__init__("Uzel")
       self.publisher_ = self.create_publisher(String, 'publisher', 10)
       self.timer = self.create_timer(1, self.timer_callback)

    def timer_callback(self):
       msg = String()
       msg.data = "Ros publisher"
       self.publisher_.publish(msg)
       self.get_logger().info(f'Отправлено:{msg.data}')

def main ():
    rclpy.init()
    node = Empty()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
  main()

