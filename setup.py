from setuptools import setup, find_packages
import os

setup(
    name='TutorialClassroom',
    version='0.1',
    author='Phil Elson',
    author_email='pelson.pub@gmail.com',
    packages=find_packages(),
    package_data={'classroom.tests': [os.path.join('sample_data', '*')]},
)
