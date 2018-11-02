from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='Web_Crawler', # a unique name for PyPI
    version='0.1',
    description='Web scraping company product information, to recommend the best product.',
    author='Disaiah Bennett',
    author_email='officialdisaiahbennett@gmail.com',
    url='https://dislbenn.github.io/web/', # http://location or https://location
    packages=['myFormat', ], # packages and subpackages containing .py files
    package_dir={'':'src'},
    package_data={'myFormat':['other/*']}, # other needed files will be installed for user
    scripts=['src/test',], # the executable files will be installed for user
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README').read(),
    # more meta-data for repository
    classifiers=[
      'Development Status :: 4 - Beta',
      'Environment :: X11 Applications :: GTK',
      'Intended Audience :: End Users/Desktop',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: GNU General Public License (GPL)',
      'Operating System :: POSIX :: Linux',
      'Programming Language :: Python',
      'Topic :: Desktop Environment',
      'Topic :: Text Processing :: Fonts'
      ],
)
