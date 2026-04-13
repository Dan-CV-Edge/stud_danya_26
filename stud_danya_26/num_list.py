import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class OverflowListener(Node):
    def __init__(self):
        super().__init__('overflow_listener')
        
        self.subscription = self.create_subscription(
            Int32,
            'overflow',
            self.listener_callback,
            10)
        self.get_logger().info('Узел-слушатель запущен и ждет переполнения...')

    def listener_callback(self, msg):
        self.get_logger().error(f'ВНИМАНИЕ! Получен сигнал переполнения: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = OverflowListener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()