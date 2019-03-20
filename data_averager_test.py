#! /usr/bin/python

import pytest
import data_averager
from mock import patch

def test_dataGrabberFail():

    fail_tests = [10, {'test': 1}, ['test'], '/some/path/to/somewhere']
    
    with patch.object(sys, 'argv', fail_tests):
        averager_result = data_averager.dataGrabber()
        assert averager_result == (
            'Please provide full filepath to USGS Geomagnetism file as an '
            'argument to be parsed.\n Example: "python data_averager.py '
            '/path/to/file"')
