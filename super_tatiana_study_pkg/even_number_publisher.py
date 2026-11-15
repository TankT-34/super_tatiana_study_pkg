#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class EvenNumberPublisher(Node):
	def __init__(self):
		super().__init__('even_pub')

		self.declare_parameter('publish_frequency', 10.0)
		self.declare_parameter('overflow_threshold', 100)
		self.declare_parameter('topic_name', 'even_numbers')
		self.declare_parameter('overflow_topic', 'overflow')

		self.freq = self.get_parameter('publish_frequency').value
		self.threshold = self.get_parameter('overflow_threshold').value
		self.topic = self.get_parameter('topic_name').value
		self.overflow_topic = self.get_parameter('overflow_topic').value

		self.publisher_ = self.create_publisher(Int32, self.topic, 10)
		self.overflow_publisher_ = self.create_publisher(Int32, self.overflow_topic, 10)

		self.timer = self.create_timer(1.0 / self.freq, self.timer_callback)

		self.counter = 0

	def timer_callback(self):
		if self.counter >= self.threshold:
			overflow_msg = Int32()
			overflow_msg.data = self.threshold
			self.overflow_publisher_.publish(overflow_msg)
			self.get_logger().warn(f'PEREPOLNENIE! POLUCHENO {self.threshold}')
			self.counter = 0
		msg = Int32()
		msg.data = self.counter
		self.publisher_.publish(msg)
		self.get_logger().info(f'PUBLICUYU: {msg.data} V TOPIC {self.topic}')
		self.counter += 2

def main(args = None):
	rclpy.init(args = args)
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
