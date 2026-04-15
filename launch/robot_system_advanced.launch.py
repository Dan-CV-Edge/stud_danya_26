
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_ros.actions import Node

def generate_launch_description():
    # Объявляем аргумент для выбора режима
    mode_arg = DeclareLaunchArgument(
        'mode',
        default_value='slow',
        description='Режим работы: fast (20Hz, порог 50) или slow (5Hz, порог 150)'
    )
    
    mode = LaunchConfiguration('mode')
    
    return LaunchDescription([
        mode_arg,
        
        Node(
            package='stud_danya_26',
            executable='number_mode',
            name='even_pub',
            output='screen',
            parameters=[
                {
                    'publish_frequency': PythonExpression([
                        "20.0 if '", mode, "' == 'fast' else 5.0"
                    ]),
                    'overflow_threshold': PythonExpression([
                        "50 if '", mode, "' == 'fast' else 150"
                    ]),
                    'topic_name': PythonExpression([
                        "'/even_numbers_fast' if '", mode, 
                        "' == 'fast' else '/even_numbers_slow'"
                    ]),
                    'overflow_topic': 'overflow',
                }
            ],
        ),
        
        Node(
            package='stud_danya_26',
            executable='num_lis',
            name='overflow_listener',
            output='screen',
            parameters=[
                {
                    'input_topic': 'overflow',
                }
            ],
        ),
    ])
