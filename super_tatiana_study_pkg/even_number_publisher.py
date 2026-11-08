#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class EvenNumberPublisher(Node):
	def __init__(self):
		super().__init__('even_pub')

		self.publisher_ = self.create_publisher(Int32, 'even_numbers', 10)
		self.overflow_publisher_ = self.create_publisher(Int32, 'overflow', 10)

		timer_period = 0.1
		self.timer = self.create_timer(timer_period, self.timer_callback)

		self.counter = 0

	def timer_callback(self):
		if self.counter >= 100:
			overflow_msg = Int32()
			overflow_msg.data = 100
			self.overflow_publisher_.publish(overflow_msg)
			self.get_logger().warn("Perepolnenie! Polucheno 100")
			self.counter = 0
		msg = Int32()
		msg.data = self.counter
		self.publisher_.publish(msg)
		self.get_logger().info(f'Polucheno: {msg.data}')
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
