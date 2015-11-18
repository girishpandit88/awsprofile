__author__ = 'girishpandit'
from setuptools import setup
import os
if os.environ.get('USER','') == 'vagrant':
    del os.link
setup(name='awsprofile',
      version='0.4',
      description='Easy way to swap aws iam profiles',
      url='https://github.com/girishpandit88/awsprofile',
      author='girishpandit',
      author_email='girschol13@gmail.com',
      license='MIT',
      packages=['awsprofile'],
      zip_safe=False,
      entry_points = {
        "console_scripts": ['awsprofile = awsprofile:main']
        })
