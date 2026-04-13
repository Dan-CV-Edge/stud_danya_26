import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32  # Тип для чисел

class EvenNumberPublisher(Node):
    def __init__(self):
        super().__init__('even_pub')
     
        self.publisher_ = self.create_publisher(Int32, 'even_numbers', 10)
        
        self.overflow_publisher_ = self.create_publisher(Int32, 'overflow', 10)
        
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.counter = 0

    def timer_callback(self):
        msg = Int32()
        msg.data = self.counter
        self.publisher_.publish(msg)
        self.get_logger().info(f'Публикация: {msg.data}')

        if self.counter >= 100:
            overflow_msg = Int32()
            overflow_msg.data = self.counter
            self.overflow_publisher_.publish(overflow_msg)
            self.get_logger().warn(f'!!! ПЕРЕПОЛНЕНИЕ !!! Значение: {self.counter}')
            self.counter = 0  # Сброс
        else:
            self.counter += 2

def main(args=None):
    rclpy.init(args=args)
    node = EvenNumberPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()