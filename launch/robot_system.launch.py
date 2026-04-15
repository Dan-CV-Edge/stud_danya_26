
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='stud_danya_26',
            executable='number_mode',
            name='even_pub',
            output='screen',
            parameters=[
                {'publish_frequency': 8.0},      # частота 8 Гц
                {'overflow_threshold': 80},      # порог 80
                {'topic_name': 'even_numbers'},
                {'overflow_topic': 'overflow'},
            ],
        ),
        Node(
            package='stud_danya_26',
            executable='num_lis',
            name='overflow_listener',
            output='screen',
            parameters=[
                {'input_topic': 'overflow'},
            ],
        ),
    ])