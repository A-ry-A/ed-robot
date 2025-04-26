#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import SetPen
from functools import partial

class TurtlecontrollerNode(Node):
    def __init__(self):
        super().__init__("turtle_controller")
        self.cmd_vel_publisher_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.pose_subscriber_ = self.create_subscription(Pose, "/turtle1/pose", self.pose_callback, 10)
        self.get_logger().info("Turtle controller has been started.")
        self.previous_x = 0.0

    def pose_callback(self, pose: Pose):
        cmd = Twist()
        if pose.x >9.0 or pose.x < 2.0 or pose.y >9.0 or pose.y < 2.0:
            cmd.linear.x = 6.0
            cmd.angular.z = 5.0
        else:
            cmd.linear.x = 6.0
            cmd.angular.z = 0.0
        self.cmd_vel_publisher_.publish(cmd)

        if pose.x > 5.5 and self.previous_x <= 5.5:
            self.get_logger().info("set color to red")
            self.call_pen_service(255,0,0,3,0)
        elif pose.x < 5.5 and self.previous_x >= 5.5:
            self.get_logger().info("set color to green")
            self.call_pen_service(0,255,0,3,0)
        
        self.previous_x = pose.x

    def call_pen_service(self, r, g ,b , width, off):
        client = self.create_client(SetPen, "/turtle1/set_pen")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for service...")
        
        request = SetPen.Request()
        request.r = r
        request.g = g
        request.b = b
        request.width = width
        request.off = off

        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_set_pen))
    
    def callback_set_pen(self,future):
        try:
            reponse = future.result()
        except Exception as e:
            self.get_logger().error("Service call failes: %r" % (e,))
        

def main(args=None):
    rclpy.init(args=args)
    node = TurtlecontrollerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()