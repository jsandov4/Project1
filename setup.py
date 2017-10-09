from distutils.core import setup

setup(name='Dynamic',
      version='1.0',
      description='Langevine dynamic program',
      author='Juan S Sandoval',
      author_email='jsandov4@ur.rochester.edu',
      url='https://github.com/jsandov4/Project1',
      packages=['dynamic'],
      entry_points = {
	'console_scripts' : ['dynamic = dynamic.__init__:main'],}
     )



