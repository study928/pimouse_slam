#!/usr/bin/env python
import tf, math
from geometry_msgs.msg import Vector3, Quaternion

def euler_to_quaternion(euler):
    """Convert Euler Angles to Quaternion

    euler: geometry_msgs/Vector3
    quaternion: geometry_msgs/Quaternion
    """
    q = tf.transformations.quaternion_from_euler(euler.x, euler.y, euler.z)
    return Quaternion(x=q[0], y=q[1], z=q[2], w=q[3])

def quaternion_to_euler(quaternion):
    """Convert Quaternion to Euler Angles

    quarternion: geometry_msgs/Quaternion
    euler: geometry_msgs/Vector3
    """
    e = tf.transformations.euler_from_quaternion((quaternion.x, quaternion.y, quaternion.z, quaternion.w))
    return Vector3(x=e[0], y=e[1], z=e[2])

if __name__ == '__main__':
    v = euler_to_quaternion(Vector3(0.0, 0.0, math.pi))
    q = quaternion_to_euler(Quaternion(0.0, 0.0, 0.0, 1.0))
    print(v)
    print(q)
    print(math.pi)
