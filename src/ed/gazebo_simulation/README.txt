To run new_ed_maze.sdf and visualise LiDAR in RViz:
1. In the terminal, run [ign gazebo new_ed_maze.sdf]
2. Press the three horizontal dots for the plugin menu, then search for "Visualise Lidar" and select it. scroll down 
   the menu on the right side, and under visualise lidar press the refresh button to see the /lidar topic
3. Go to the plugin menu again and search for "Key Publisher" and select it.
4. Run the simulation.
5. In a new tab in your terminal, run [ros2 run ros_gz_bridge parameter_bridge /keyboard/keypress@std_msgs/msg/Int32@ignition.msgs.Int32]
   If successful you should see:
   [INFO] [1748338905.858174926] [ros_gz_bridge]: Creating GZ->ROS Bridge: [/keyboard/keypress (ignition.msgs.Int32) -> /keyboard/keypress (std_msgs/msg/Int32)] (Lazy 0)
   [INFO] [1748338905.860777327] [ros_gz_bridge]: Creating ROS->GZ Bridge: [/keyboard/keypress (std_msgs/msg/Int32) -> /keyboard/keypress (ignition.msgs.Int32)] (Lazy 0)
6. In a new tab in your terminal, run [ros2 run ros_gz_bridge parameter_bridge /lidar@sensor_msgs/msg/LaserScan@ignition.msgs.LaserScan].
   A similar message should appear to the one for the previous step.
7. In a new tab in your terminal, run [ros2 run tf2_ros static_transform_publisher \0 0 0 0 0 0 base_link Ed_Robot/chassis/gpu_lidar]
   The output should be:
   [WARN] [1748339271.392556221] []: Old-style arguments are deprecated; see --help for new-style arguments
   [INFO] [1748339271.746741458] [static_transform_publisher_95cKP0XnlXdJHk1X]: Spinning until stopped - publishing transform
   translation: ('0.000000', '0.000000', '0.000000')
   rotation: ('0.000000', '0.000000', '0.000000', '1.000000')
   from 'base_link' to 'Ed_Robot/chassis/gpu_lidar'
8. In a new tab, run RViz by running [rviz2]
9. In RViz, select Ed_Robot/chassis/gpu_lidar as the fixed frame. 
10. Press the Add button, navigate to the "By topic" tab, and and select LaserScan. Click OK.
11. In the drop-down for LaserScan, select Points for the Style.
12. Move the robot in Gazebo, and the LiDAR should be visualised in RViz.

