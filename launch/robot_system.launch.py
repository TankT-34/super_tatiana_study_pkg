#!/usr/bin/env python3

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
	freq_arg = DeclareLaunchArgument('publish_frequency', default_value = '8.0', description = 'CHASTOTA (Hz)')
	threshold_arg = DeclareLaunchArgument('overflow_threshold', default_value = '80', description = 'POROG PEREPOLNENIYA')
	topic_arg = DeclareLaunchArgument('topic_name', default_value = 'even_numbers', description = 'IMYA TOPIKA')
	node_name_arg = DeclareLaunchArgument('node_name', default_value = 'even_pub')
	listener_name_arg = DeclareLaunchArgument('listener_name', default_value = 'overflow_listener')
	overflow_topic_arg = DeclareLaunchArgument('overflow_topic', default_value = 'overflow')

	frequency = LaunchConfiguration('publish_frequency')
	threshold = LaunchConfiguration('overflow_threshold')
	topic = LaunchConfiguration('topic_name')
	node_name = LaunchConfiguration('node_name')
	listener_name = LaunchConfiguration('listener_name')
	overflow_topic = LaunchConfiguration('overflow_topic')

	return LaunchDescription([
		freq_arg,
		threshold_arg,
		topic_arg,
		node_name_arg,
		listener_name_arg,
		overflow_topic_arg,

		Node(
			package = 'super_tatiana_study_pkg',
			executable = 'even_publisher',
			name = node_name,
			parameters = [{
				'publish_frequency': frequency,
				'overflow_threshold': threshold,
				'topic_name': topic,
				'overflow_topic': overflow_topic,
			}],
			output = 'screen',
		),
		Node(
			package = 'super_tatiana_study_pkg',
			executable = 'overflow_listener',
			name = listener_name,
			parameters = [{
				'overflow_topic': overflow_topic,
			}],
			output = 'screen',
		),
	])
