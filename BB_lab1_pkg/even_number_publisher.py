
#!/usr/bin/env python3
import rclpy                     
from rclpy.node import Node        
from std_msgs.msg import Int32    


class EvenPublisher(Node):

    def __init__(self):
        # Даём узлу имя "even_pub"
        super().__init__('even_pub')
        self.current_num = 0

        self.publisher_1 = self.create_publisher(Int32, 'even_numbers', 10)
        self.publisher_2 = self.create_publisher(Int32, 'overflow', 10)

        timer_period = 0.1          
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.get_logger().info("Узел even_pub запущен!")


    def timer_callback(self):
        
        even_msg = Int32() 
        overflow_msg = Int32() 
        
        overflow_msg.data = 100
        even_msg.data = self.current_num 
        
        self.publisher_1.publish(even_msg)      
        
        self.get_logger().info(f"{even_msg.data} has published to even_numbers topic")  
         
        self.current_num += 2
        
        if self.current_num == 100:
            self.publisher_2.publish(overflow_msg)  
            self.current_num = 0
            

def main():
    rclpy.init()                    # начинаем работать с ROS 2


    node = EvenPublisher()                 # создаём наш узел

    try:
        rclpy.spin(node)            # "крутимся" и ждём событий (таймеров, сообщений и т.д.)
    except KeyboardInterrupt:
        pass                        # если нажали Ctrl+C — нормально выходим
    finally:
        node.destroy_node()         # убираем узел
        rclpy.shutdown()            # завершаем ROS 2


if __name__ == '__main__':
    main()
