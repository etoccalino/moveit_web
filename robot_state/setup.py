from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup()
d['packages'] = ['moveit_web_robot_state']
d['scripts'] = []
d['package_dir'] = {'': 'python'}

setup(**d)
