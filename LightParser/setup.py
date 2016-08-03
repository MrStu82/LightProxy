#!/usr/bin/env python

from setuptools import setup, find_packages
try:
    import py2exe
except:
    pass


setup(name='LightParser',
      version='1.0',
      description='Light Data Parser',
      author='Youness Alaoui',
      author_email='mrstu@me.com',
      url='https://github.com/MrStu82/LightProxy',
      packages=find_packages(),
      console = ['parser.py']
     )
