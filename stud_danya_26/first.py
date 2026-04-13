import rclpy
from rclpy.node import Node

def main(args=None):
    rclpy.init(args=args)                 
    node = Node('hello_node')           
    node.get_logger().info("Hello ROS 2 World! 🚀")
    rclpy.spin(node)                       
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()