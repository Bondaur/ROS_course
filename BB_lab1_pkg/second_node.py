#!/usr/bin/env python3
"""Первый узел ROS 2 — Hello World"""

import rclpy
import time

from rclpy.node import Node


def main(args=None):
    rclpy.init(args=args)                   # инициализация ROS 2
    node = Node('five_sec_timer')              
    
    def TimerPrint():
        current_struct = time.localtime()
        # Format it (e.g., HH:MM:SS)
        formatted_time = time.strftime("%H:%M:%S", current_struct)
        node.get_logger().info(formatted_time)
    
    node.create_timer(5,TimerPrint)
    rclpy.spin(node)                        # запускаем цикл обработки
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()