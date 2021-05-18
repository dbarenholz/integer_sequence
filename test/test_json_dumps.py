# -*- coding: utf-8 -*-
from typing import Any
import sys
import os
import time

# Make pytest find our tests and modules
sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/.."))

# Own
from helper import loads, dumps, assert_equal, TESTPATH


def single_case(test_id: str, test_object: Any):
    """
    Performs a dump and load for a particular object and asserts they are equal.
    """
    # Dump to disk
    path = os.path.join(TESTPATH, f"{time.strftime('%Y%m%d-%H%M%S')} - {test_id}")
    success = dumps(filename=path, data=test_object)

    # Ensure that dumping is successful
    assert_equal(True, success)

    # Read from disk
    reloaded_object = loads(path)

    assert_equal(True, test_object == reloaded_object)

    # Cleanup
    os.remove(f"{path}.pkl")


def test_runner():
    """
    Single method with all testcases for dump and loading functionality.
    """
    # Dictionary holding all testcases
    testcases = {
        "dictionary-empty": dict(),
        "dictionary-nonempty": {k: k ** 2 for k in range(10)},
        "list-empty": list(),
        "list-nonempty": list(range(10)),
        "integer": 5,
        "string": "hi there",
        "bool": False,
        "set-empty": set(),
        "set-nonempty": set([1, 2, 3]),
        "generator": range(10),
        "complex_object": {
            "something": 5,
            "with_lists": [[1, 2, 3], ["a"], [], []],
            "and_more": set(),
        },
    }
    """Dictionary that contains all testcases, with the ID being the key and the object to serialize being the value"""

    # Do all tests.
    for (test_id, test_object) in testcases.items():
        single_case(test_id=test_id, test_object=test_object)
