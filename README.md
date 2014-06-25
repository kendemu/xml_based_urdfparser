xml_based_urdfparser
====================

a python urdf parser based on xml minidom


Features
========

Generate urdf and xacro files for aldebaran robots (using Aldebaran URDFs as input files https://github.com/keulYSMB/nao_robot/tree/devel/nao_description/bin)
Automatic generation of the entire URDF file or of specific parts of the robot as xacro files.

Dependencies 
============

xml.dom
argparse
subprocess
the library provided in this package

Changes
=======

- add transmission and gazebo tags to the parser library
- add methods to library : add_material, add_gazebo
- export xacro files using kinematics chains
- fix scale of meshes in the output files

TODO
======
- find a way to simulate nao in Gazebo (for now it is falling through the ground)
- get finger Frames and SensorFrames from aldebaran documentation
- fix joints:
    - get L/RHand from documentation : limits
    - mimic joints for pelvis and fingers
- add sensor plugins for gazebo tags
