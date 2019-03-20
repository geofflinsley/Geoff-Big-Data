#! /usr/bin/python

import pytest
import data_averager
from mock import patch

def test_dataGrabberFail():

    fail_tests = [10, {'test': 1}, ['test'], '/some/path/to/somewhere']
    
    with patch.object(sys, 'argv', fail_tests):
        averager_result = data_averager.dataGrabber()
        assert averager_result == None


def test_dataGrabberPass():
    
    pass_test = '/home/apesch/geoff_sample_data.txt'
    
    with patch.object(sys, 'argv', pass_test):
        averager_result = data_averager.dataGrabber()
        assert type(averager_result) == list
        assert len(averager_result) > 1