from distutils.core import setup

setup(name='Dynamics',
      version='1.0',
      description='Langevine dynamic program',
      author='Juan S Sandoval',
      author_email='jsandov4@ur.rochester.net',
      url='https://www.python.org/sigs/distutils-sig/',
      packages=['dynamic'],
      { 
	'console_script' : ['dynamic = dynamic.lans:start']
	}

     )



