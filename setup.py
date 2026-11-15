from setuptools import find_packages, setup

package_name = 'super_tatiana_study_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
	('share/' + package_name + '/launch', ['launch/my_first_launch.py', 'launch/robot_system.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tatiana',
    maintainer_email='tatiana@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
		'first_node = super_tatiana_study_pkg.first_node:main',
		'time_printer = super_tatiana_study_pkg.time_printer:main',
		'even_publisher = super_tatiana_study_pkg.even_number_publisher:main',
		'overflow_listener = super_tatiana_study_pkg.overflow_listener:main',
        ],
    },
)
