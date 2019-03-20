#! /usr/bin/python

import pytest
import data_averager

def test_dataGrabberFail():

    fail_tests = [10, {'test': 1}, ['test'], '/some/path/to/somewhere']
    
    for test in fail_tests:
        assert data_averager.dataGrabber(test) == (
            'Please provide full filepath to USGS Geomagnetism file as an '
            'argument to be parsed.\n Example: "python data_averager.py ' 
            '/path/to/file"')
