#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class EvenNumberPublisher(Node):
    def __init__(self):
        super().__init__('even_pub')
        
        # Объявляем параметры
        self.declare_parameter('publish_frequency', 10.0)   # Гц
        self.declare_parameter('overflow_threshold', 100)   # порог
        self.declare_parameter('topic_name', 'even_numbers')
        self.declare_parameter('overflow_topic', 'overflow')
        
        # Читаем параметры
        freq = self.get_parameter('publish_frequency').value
        self.threshold = self.get_parameter('overflow_threshold').value
        self.topic = self.get_parameter('topic_name').value
        self.overflow_topic = self.get_parameter('overflow_topic').value
        
        self.publisher_ = self.create_publisher(Int32, self.topic, 10)
        self.overflow_publisher_ = self.create_publisher(Int32, self.overflow_topic, 10)
        
        # Таймер с частотой из параметра
        self.timer = self.create_timer(1.0 / freq, self.timer_callback)
        self.counter = 0
        
        self.get_logger().info(f'Публикатор запущен: частота={freq}Гц, порог={self.threshold}, топик={self.topic}')

    def timer_callback(self):
        msg = Int32()
        msg.data = self.counter
        self.publisher_.publish(msg)
        self.get_logger().info(f'Публикация: {msg.data}')

        if self.counter >= self.threshold:
            overflow_msg = Int32()
            overflow_msg.data = self.counter
            self.overflow_publisher_.publish(overflow_msg)
            self.get_logger().warn(f'!!! ПЕРЕПОЛНЕНИЕ !!! Значение: {self.counter}')
            self.counter = 0
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