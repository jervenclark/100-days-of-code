#!/usr/bin/python

import sys, os

if ( len(sys.argv) < 2):
    print 'Please provide project name'
else:
    day = len(os.listdir('src'))
    os.mkdir("src/{:0>2d}-".format(day) + str(sys.argv[1]))
