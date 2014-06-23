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

TODO
======

- get finger Frames and SensorFrames from aldebaran documentation
- add transmission and gazebo tags to the parser library
- fix joints:
    - get L/RHand from documentation : limits
    - mimic joints for pelvis and fingers
