#!/usr/bin/env python3

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
	mode_arg = DeclareLaunchArgument('mode', default_value = 'fast', description = 'Rezhim raboty: fast (dlya otladki) ili slow (normalniy)')
	mode = LaunchConfiguration('mode')

	def launch_setup(context, *args, **kwargs):
		mode_val = mode.perform(context)

		if mode_val == 'fast':
			frequency = 20.0
			threshold = 50
			topic = '/even_numbers_fast'
		else:
			frequency = 5.0
			threshold = 150
			topic = '/even_numbers_slow'

		return [
			Node(
				package = 'super_tatiana_study_pkg',
				executable = 'even_publisher',
				name = 'even_pub',
				parameters = [{
					'publish_frequency': frequency,
					'overflow_threshold': threshold,
					'topic_name': topic,
				}],
				output = 'screen',
			),
			Node(
				package = 'super_tatiana_study_pkg',
				executable = 'overflow_listener',
				name = 'overflow_listener',
				output = 'screen',
			),
		]

	return LaunchDescription([
		mode_arg,
		OpaqueFunction(function = launch_setup),
	])
