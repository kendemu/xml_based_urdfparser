#!/usr/bin/env python

from distutils.core import setup

d = {'author': u'Mikael Arguedas <mikael.arguedas@gmail.com>',
 'description': 'This package contains a Python implementation of the\nurdf_parser modeling various aspects of robot information, specified in the\nXml Robot Description Format (URDF). and Gazebo simulator',
 'license': 'BSD',
 'maintainer': u'Mikael Arguedas',
 'maintainer_email': 'mikael.arguedas@gmail.com',
 'name': 'xmlbased_URDF_parser',
 'package_dir': {'': 'src'},
 'packages': ['xmlURDFParser'],
 'url': 'http://ros.org/wiki/???',
 'version': '0.1.0'}

setup(**d)
