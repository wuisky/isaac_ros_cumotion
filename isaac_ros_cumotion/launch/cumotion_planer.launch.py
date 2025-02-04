from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():
    current_directory = os.getcwd()
    urdf_path = os.path.join(
        os.getenv('ISAAC_ROS_WS'),
        'src/isaac_ros_cumotion/curobo_core/curobo/src/curobo/content/assets/robot/ur_description/ur5e.urdf'
    )

    return LaunchDescription([
        Node(
            package='isaac_ros_cumotion',
            executable='cumotion_planner_node',
            name='cumotion_planner_node',
            output='screen',
            parameters=[
                {'robot': 'ur5e_preset_tool0_sphere.xrdf'},
                {'urdf_path': urdf_path},
                {'publish_robot_as_spheres': False},
            ]
        )
    ])
