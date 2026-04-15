from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='stud_danya_26',          
            executable='number_mode',
            name='event_pub',
            output='screen',
        ),
        Node(
            package='stud_danya_26',
            executable='num_lis',
            name='listener',
            output='screen',
        ),
    ])