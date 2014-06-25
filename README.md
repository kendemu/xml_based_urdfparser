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
nao_meshes package if you want the official Aldebaran meshes

Changes
=======
06/25/2014
- add transmission and gazebo tags to the parser library
- add methods to library : add_material, add_gazebo
- export xacro files using kinematics chains
- fix scale of meshes in the output files
- New impu parameter : --meshes

TODO
======
- add transmission to urdf + ros_controller to perform real simulation 
- get finger Frames and SensorFrames from aldebaran documentation
- fix joints:
    - get L/RHand from documentation : limits
    - mimic joints for pelvis and fingers
- add sensor plugins for gazebo tags
- improve exportXacroRobotChain function

Missing Resources
=================
- Finger and toes frames from Aldebaran doc
- Transmission elements
- Missing mimic joints (we can add them by hand for know)

