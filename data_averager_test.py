#! /usr/bin/python

import pytest
import data_averager

def test_dataGrabberFail():

    fail_tests = [10, {'test': 1}, ['test'], '/some/path/to/somewhere']
    
    with pytest.raises(Exception):
        for test in fail_tests:
            data_averager.dataGrabber(test)