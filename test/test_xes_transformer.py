# -*- coding: utf-8 -*-
import sys
import os
import pytest

# Make pytest find our tests and modules
sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/.."))

# Own
from helper import assert_equal
from generator import XESTransformator
from exception import InvalidLogFormat, ParsingError
from helper import TESTPATH
from sequences import EXAMPLE_LOG_AS_INTS


def test_invalid_log():
    # The logs to test.
    logs = [
        os.path.join(os.path.join(TESTPATH, "logs"), "invalid_log.xes"),
        os.path.join(os.path.join(TESTPATH, "logs"), "invalid_log.xes.gz"),
    ]

    # Create a transformator
    transformator = XESTransformator()

    # Loop through logs
    for log in logs:

        # Expect an error to be raised here
        with pytest.raises(ParsingError):
            transformator.transform(log)


def test_invalid_extension():
    # The log to test (need to use [0] to select first element from tuple)
    log = (
        os.path.join(
            os.path.join(TESTPATH, "logs"), "valid_xes_wrong_extension.cool_log_format"
        ),
    )[0]

    # Create a transformator
    transformator = XESTransformator()

    # Expect an error to be raised here
    with pytest.raises(InvalidLogFormat):
        transformator.transform(log)


def test_valid_logs():
    # The logs to test.
    logs = [
        os.path.join(os.path.join(TESTPATH, "logs"), "sample_log.xes"),
        os.path.join(os.path.join(TESTPATH, "logs"), "sample_log.xes.gz"),
    ]

    # Create a transformator
    transformator = XESTransformator()

    # Loop through logs
    for log in logs:

        transformed = transformator.transform(log)
        assert_equal(EXAMPLE_LOG_AS_INTS, transformed)
