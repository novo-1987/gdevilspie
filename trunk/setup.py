#!/usr/bin/env python

from distutils.core import setup

setup(name='gdevilspie',
      version='0.1',
      description='GTK GUI for devilspie',
      author='Islam Amer',
      author_email='iamer@open-craft.com',
      url='http://code.google.com/p/gdevilspie/',
	  license='GPLv2',
      py_modules=['parser', 'reader','filler'],
	  scripts=['./gdevilspie.py'],
	  data_files=[('data',['./gdevilspie.glade', './window-new.png'])],
     )
#we need to clean the dir heirarchy; root includes only py files and README, icon and .glade go to data subdirs. also i dunno if the script is made system-wide excutable or not.
#FIXME: Add data/ subdir and move non py stuff there.

