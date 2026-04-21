#!/usr/bin/env python3
import rclpy                     
from rclpy.node import Node        
from std_msgs.msg import Int32     

class OverflowListener(Node):

    def __init__(self):
    
        super().__init__('overflow_listener')

        self.subscription = self.create_subscription(
            Int32,
            'overflow',
            self.callback,
            10)

        self.get_logger().info("Узел overflow_listener запущен и слушает топик overflow!")

    def callback(self, msg):
        self.get_logger().warn(f"!!! OVERFLOW DETECTED !!!: Got value {msg.data}")

def main():
    rclpy.init()                    # стартуем ROS 2
    node = OverflowListener()               # создаём наш узел
    try:
        rclpy.spin(node)            # крутимся и ждём сообщений
    except KeyboardInterrupt:
        pass                        # Ctrl+C — нормально выходим
    finally:
        node.destroy_node()         # убираем узел
        rclpy.shutdown()            # завершаем ROS 2

if __name__ == '__main__':
    main()