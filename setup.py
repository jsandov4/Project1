from distutils.core import setup

with open('README.md') as f:
    long_description = ''.join(f.readlines())

# get the dependencies and installs
with open('requirements.txt') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]


setup(name='Dynamic',
      version='1.0',
      description='Langevine dynamic program',
      long_description=long_description,
      author='Juan S Sandoval',
      author_email='jsandov4@ur.rochester.edu',
      url='https://github.com/jsandov4/Project1',
      packages=['dynamic'],
      install_requires=install_requires,
      entry_points = {
	'console_scripts' : ['dynamic = dynamic.__init__:main'],
      }
     )



