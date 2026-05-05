#!/usr/bin/env python3
import rclpy                        
from rclpy.node import Node         
from std_msgs.msg import String     

class Listener(Node):

    def __init__(self):

        super().__init__('listener')


        self.subscription = self.create_subscription(
            String,
            'my_chat_topic',
            self.callback,
            10)

        self.get_logger().info("Узел listener запущен и слушает топик!")


    def callback(self, msg):
       
        self.get_logger().info(f"Я услышал: {msg.data}")

def main():
    rclpy.init()                    
    node = Listener()               
    try:
        rclpy.spin(node)            
    except KeyboardInterrupt:
        pass                        
    finally:
        node.destroy_node()         
        rclpy.shutdown()            

if __name__ == '__main__':
    main()