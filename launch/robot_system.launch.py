
#!/usr/bin/env python3

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    
    mode_arg = DeclareLaunchArgument(
        'mode',
        default_value='slow',
        description="Режим работы"
    )

    node_1_name_arg = DeclareLaunchArgument(
        'node_1_name',
        default_value='even_pub',
        description="Имя узла-публикатора"
    )

    freq_arg = DeclareLaunchArgument(
        'publish_frequency',
        default_value='5.0' if mode_arg=='slow' else '20.0',
        description="Частота публикации чисел"
    )

    threshold_arg = DeclareLaunchArgument(
        'overflow_threshold',
        default_value='150',
        description='Порог переполнения'
    )

    topic_1_name_arg = DeclareLaunchArgument(
        'topic_1_name',
        default_value='even_numbers',
        description="Имя топика с чётными числами"
    )

    topic_2_name_arg = DeclareLaunchArgument(
        'topic_2_name',
        default_value='overflow',
        description="Имя топика переполнения"
    )

    node_2_name_arg = DeclareLaunchArgument(
        'node_2_name',
        default_value='overflow_listener',
        description="Имя узла-подписчика"
    )


    node_1 =  Node(
            package='BB_lab1_pkg',
            executable='even_pub',
            name=LaunchConfiguration('node_1_name'),
            output='screen',
            parameters=[
                {'publish_frequency': LaunchConfiguration('publish_frequency')},           # float
                {'overflow_threshold': LaunchConfiguration('overflow_threshold')},           # int
                {'topic_1_name': LaunchConfiguration('topic_1_name')}, # string
                {'topic_2_name': LaunchConfiguration('topic_2_name')}, # string
            ],
        )
    
    node_2 = Node(
            package='BB_lab1_pkg',
            executable='overflow_listener',
            name=LaunchConfiguration('node_2_name'),
            output='screen',
            parameters=[
                {'topic_2_name': LaunchConfiguration('topic_2_name')}, # string
            ],
    )
    
    return LaunchDescription([
        mode_arg,
        node_1_name_arg,
        node_2_name_arg,
        freq_arg,
        threshold_arg,
        topic_1_name_arg,
        topic_2_name_arg,
        node_1,
        node_2  
    ])
