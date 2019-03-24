#!/usr/bin/python

import sys, os, shutil

if ( len(sys.argv) < 2):
    print('Please provide project name')
else:
    day = len(os.listdir('src'))
    shutil.copytree("template", "src/{:0>2d}-".format(day) + str(sys.argv[1]))
