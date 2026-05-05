
#!/usr/bin/env python3
import rclpy                     
from rclpy.node import Node        
from std_msgs.msg import Int32    


class EvenPublisher(Node):

    def __init__(self):

        super().__init__("even_pub")


        self.declare_parameter('publish_frequency', 10.0) 
        self.declare_parameter('overflow_threshold', 100)
        self.declare_parameter('topic_1_name', '/even_numbers')
        self.declare_parameter('topic_2_name', '/overflow')

        self.freq = self.get_parameter('publish_frequency').value
        self.threshold = self.get_parameter('overflow_threshold').value
        self.topic_1 = self.get_parameter('topic_1_name').value
        self.topic_2 = self.get_parameter('topic_2_name').value

        self.publisher_1 = self.create_publisher(Int32, self.topic_1, 10)
        self.publisher_2 = self.create_publisher(Int32, self.topic_2, 10)
        self.timer = self.create_timer(1.0 / self.freq, self.timer_callback)

        self.current_num = 0

        #self.publisher_1 = self.create_publisher(Int32, 'even_numbers', 10)
        #self.publisher_2 = self.create_publisher(Int32, 'overflow', 10)

        #timer_period = 0.1          
        #self.timer = self.create_timer(timer_period, self.timer_callback)

        self.get_logger().info(f"Узел {self.get_name()} запущен с параметрами {self.freq}, {self.threshold}, {self.topic_1}, {self.topic_2}")


    def timer_callback(self):
        
        even_msg = Int32() 
        overflow_msg = Int32() 
        
        overflow_msg.data = self.threshold
        even_msg.data = self.current_num 
        
        self.publisher_1.publish(even_msg)      
        
        self.get_logger().info(f"{even_msg.data} has published to {self.topic_1} topic")  
         
        self.current_num += 2
        
        if self.current_num == self.threshold:
            self.publisher_2.publish(overflow_msg)  
            self.current_num = 0
            

def main():
    rclpy.init()                  


    node = EvenPublisher()               

    try:
        rclpy.spin(node)       
    except KeyboardInterrupt:
        pass                      
    finally:
        node.destroy_node()        
        rclpy.shutdown()            


if __name__ == '__main__':
    main()
