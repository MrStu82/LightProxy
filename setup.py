#!/usr/bin/env python

from distutils.core import setup
import glob
try:
    import py2exe
except:
    pass

plugin_patterns = ('plugins/*.py', 'plugins/*.yapsy-plugin')
plugins = []
for pattern in plugin_patterns:
    plugins.extend(glob.glob(pattern))

setup(name='LightParser',
      version='1.0',
      description='Light Data Parser',
      author='Youness Alaoui',
      author_email='mrstu@me.com',
      url='https://github.com/MrStu82/LightProxy',
      packages = ['LightParser', 'LightParser.gui'],
      options={"py2exe":{"optimize":2,"includes":["sip"], "dll_excludes": ["MSVCP90.dll"]}},
      console = ['LightParser.py', 'LightProxy.py'],
      data_files=[('plugins', plugins)],
     )
