# -*- coding: utf-8 -*-
import sys
import os
import pytest

# Make pytest find our tests and modules
sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/.."))

# Own
from helper import assert_equal
from generator import SequenceGenerator
from exception import (
    InvalidLengthException,
    NotYetImplemented,
    MissingRequiredParameter,
)
from sequences import FIB, PASCAL, CATALAN, RECAMAN, UP, DOWN, LONGTERM

# Incorrect initialisation
def negative_length_should_raise_test() -> None:
    """
    Initialising with a strictly negative length should raise the InvalidLengthException,
    as generating lists of negative length makes no sense.
    """
    with pytest.raises(InvalidLengthException):
        SequenceGenerator(wanted_length=-5)


def zero_length_should_raise_test() -> None:
    """
    Initialising with a strictly negative length should raise the InvalidLengthException,
    as generating empty lists in this project makes no sense.
    """
    with pytest.raises(InvalidLengthException):
        SequenceGenerator(wanted_length=0)


# Incorrect generate_trace calls
def nonexistent_trace(generator: SequenceGenerator) -> None:
    """
    A call to `SequenceGenerator.generate_trace()` with unknown sequence key `seq_name` parameter should throw `NotYetImplemented`.
    This test also tests that parameters that are not required can be safely added, since the program ignores them.
    """
    with pytest.raises(NotYetImplemented):
        # Error: Incorrect key for not implemented sequence generation method
        # Ignored: Supplied 'i_do_not_matter' parameter
        generator.generate_trace("i_dont_exist", i_do_not_matter=True)


def fib_trace_missing_param(generator: SequenceGenerator) -> None:
    """
    A call to `SequenceGenerator.generate_trace()` with known sequence key `seq_name` parameter,
    but missing other parameters should throw `MissingRequiredParameter`.
    This test also tests that parameters that are not required can be safely added, since the program ignores them.
    """
    with pytest.raises(MissingRequiredParameter):
        # Error: Missing 'first', 'second' parameter
        # Ignored: Supplied 'i_do_not_matter' parameter
        generator.generate_trace("fib", i_do_not_matter=True)


def pascal_trace_missing_param(generator: SequenceGenerator) -> None:
    """
    A call to `SequenceGenerator.generate_trace()` with known sequence key `seq_name` parameter,
    but missing other parameters should throw `MissingRequiredParameter`.
    This test also tests that parameters that are not required can be safely added, since the program ignores them.
    """
    with pytest.raises(MissingRequiredParameter):
        # Error: Missing 'first' parameter
        # Ignored: Supplied 'i_do_not_matter' parameter
        generator.generate_trace("pascal", i_do_not_matter=True)


def recaman_trace_missing_param(generator: SequenceGenerator) -> None:
    """
    A call to `SequenceGenerator.generate_trace()` with known sequence key `seq_name` parameter,
    but missing other parameters should throw `MissingRequiredParameter`.
    This test also tests that parameters that are not required can be safely added, since the program ignores them.
    """
    with pytest.raises(MissingRequiredParameter):
        # Error: Missing 'first' parameter
        # Ignored: Supplied 'i_do_not_matter' parameter
        generator.generate_trace("recaman", i_do_not_matter=True)


def catalan_trace_missing_param(generator: SequenceGenerator) -> None:
    """
    A call to `SequenceGenerator.generate_trace()` with known sequence key `seq_name` parameter,
    but missing other parameters should throw `MissingRequiredParameter`.
    This test also tests that parameters that are not required can be safely added, since the program ignores them.
    """
    with pytest.raises(MissingRequiredParameter):
        # Error: Missing 'first' parameter
        # Ignored: Supplied 'i_do_not_matter' parameter
        generator.generate_trace("catalan", i_do_not_matter=True)


def range_up_missing_param(generator: SequenceGenerator) -> None:
    """
    A call to `SequenceGenerator.generate_trace()` with known sequence key `seq_name` parameter,
    but missing other parameters should throw `MissingRequiredParameter`.
    This test also tests that parameters that are not required can be safely added, since the program ignores them.
    """
    with pytest.raises(MissingRequiredParameter):
        # Error: Missing 'first', 'step' parameter
        # Ignored: Supplied 'i_do_not_matter' parameter
        generator.generate_trace("range_up", i_do_not_matter=True)


def range_down_missing_param(generator: SequenceGenerator) -> None:
    """
    A call to `SequenceGenerator.generate_trace()` with known sequence key `seq_name` parameter,
    but missing other parameters should throw `MissingRequiredParameter`.
    This test also tests that parameters that are not required can be safely added, since the program ignores them.
    """
    with pytest.raises(MissingRequiredParameter):
        # Error: Missing 'last', 'step' parameter
        # Ignored: Supplied 'i_do_not_matter' parameter
        generator.generate_trace("range_down", i_do_not_matter=True)


def long_dependency_missing_param(generator: SequenceGenerator) -> None:
    """
    A call to `SequenceGenerator.generate_trace()` with known sequence key `seq_name` parameter,
    but missing other parameters should throw `MissingRequiredParameter`.
    This test also tests that parameters that are not required can be safely added, since the program ignores them.
    """
    with pytest.raises(MissingRequiredParameter):
        # Error: Missing 'first', 'second', 'third', 'fourth', 'fifth' parameter
        # Ignored: Supplied 'i_do_not_matter' parameter
        generator.generate_trace("long_term_dependency", i_do_not_matter=True)


# Correct generate_trace calls
def fib_trace(generator: SequenceGenerator) -> None:
    """
    A call to `SequenceGenerator.generate_trace()` with known sequence key `seq_name` parameter,
    and required other parameters for the `fib` sequence generator. Test case is the default sequence list.
    This test also tests that parameters that are not required can be safely added, since the program ignores them.
    """
    expected = FIB[0 : generator.length]
    result = list(generator.generate_trace("fib", first=1, second=1))
    assert_equal(expected, result)


def pascal_trace(generator: SequenceGenerator) -> None:
    """
    A call to `SequenceGenerator.generate_trace()` with known sequence key `seq_name` parameter,
    and required other parameters for the `pascal` sequence generator. Test case is the default sequence list.
    This test also tests that parameters that are not required can be safely added, since the program ignores them.
    """
    expected = PASCAL[0 : generator.length]
    result = list(generator.generate_trace("pascal", first=1))
    assert_equal(expected, result)


def recaman_trace(generator: SequenceGenerator) -> None:
    """
    A call to `SequenceGenerator.generate_trace()` with known sequence key `seq_name` parameter,
    and required other parameters for the `recaman` sequence generator. Test case is the default sequence list.
    This test also tests that parameters that are not required can be safely added, since the program ignores them.
    """
    expected = RECAMAN[0 : generator.length]
    result = list(generator.generate_trace("recaman", first=0))
    assert_equal(expected, result)


def catalan_trace(generator: SequenceGenerator) -> None:
    """
    A call to `SequenceGenerator.generate_trace()` with known sequence key `seq_name` parameter,
    and required other parameters for the `catalan` sequence generator. Test case is the default sequence list.
    This test also tests that parameters that are not required can be safely added, since the program ignores them.
    """
    expected = CATALAN[0 : generator.length]
    result = list(generator.generate_trace("catalan", first=1))
    assert_equal(expected, result)


def range_up_trace(generator: SequenceGenerator) -> None:
    """
    A call to `SequenceGenerator.generate_trace()` with known sequence key `seq_name` parameter,
    and required other parameters for the `range_up` sequence generator. Test case is the default sequence list.
    This test also tests that parameters that are not required can be safely added, since the program ignores them.
    """
    expected = UP[0 : generator.length]
    result = list(generator.generate_trace("range_up", first=1, step=1))
    assert_equal(expected, result)


def range_down_trace(generator: SequenceGenerator) -> None:
    """
    A call to `SequenceGenerator.generate_trace()` with known sequence key `seq_name` parameter,
    and required other parameters for the `range_down` sequence generator. Test case is the default sequence list.
    This test also tests that parameters that are not required can be safely added, since the program ignores them.
    """
    expected = DOWN[-generator.length :]
    result = list(generator.generate_trace("range_down", last=1, step=1))
    assert_equal(expected, result)


def long_dependency_trace(generator: SequenceGenerator) -> None:
    """
    A call to `SequenceGenerator.generate_trace()` with known sequence key `seq_name` parameter,
    and required other parameters for the `long_term_dependency` sequence generator. Test case is the default sequence list.
    This test also tests that parameters that are not required can be safely added, since the program ignores them.
    """
    expected = LONGTERM[0 : generator.length]
    result = list(
        generator.generate_trace(
            "long_term_dependency", first=1, second=2, third=3, fourth=4, fifth=5
        )
    )
    assert_equal(expected, result)


# Incorrect generate_log calls
def nonexistent_log(generator: SequenceGenerator) -> None:
    """
    A call to `SequenceGenerator.generate_log()` with unknown sequence key `seq_name` parameter should throw `NotYetImplemented`.
    This test also tests that parameters that are not required can be safely added, since the program ignores them.
    """
    with pytest.raises(NotYetImplemented):
        # Error: Incorrect key for not implemented sequence generation method
        # Ignored: Supplied 'i_do_not_matter' parameter
        generator.generate_log("i_dont_exist", i_do_not_matter=True)


def fib_log_missing_param(generator: SequenceGenerator) -> None:
    """
    A call to `SequenceGenerator.generate_log()` with known sequence key `seq_name` parameter,
    but missing other parameters should throw `MissingRequiredParameter`.
    This test also tests that parameters that are not required can be safely added, since the program ignores them.
    """
    with pytest.raises(MissingRequiredParameter):
        # Error: Missing 'first', 'second' parameter
        # Ignored: Supplied 'i_do_not_matter' parameter
        generator.generate_log("fib", i_do_not_matter=True)


def pascal_log_missing_param(generator: SequenceGenerator) -> None:
    """
    A call to `SequenceGenerator.generate_log()` with known sequence key `seq_name` parameter,
    but missing other parameters should throw `MissingRequiredParameter`.
    This test also tests that parameters that are not required can be safely added, since the program ignores them.
    """
    with pytest.raises(MissingRequiredParameter):
        # Error: Missing 'first' parameter
        # Ignored: Supplied 'i_do_not_matter' parameter
        generator.generate_log("pascal", i_do_not_matter=True)


def recaman_log_missing_param(generator: SequenceGenerator) -> None:
    """
    A call to `SequenceGenerator.generate_log()` with known sequence key `seq_name` parameter,
    but missing other parameters should throw `MissingRequiredParameter`.
    This test also tests that parameters that are not required can be safely added, since the program ignores them.
    """
    with pytest.raises(MissingRequiredParameter):
        # Error: Missing 'first' parameter
        # Ignored: Supplied 'i_do_not_matter' parameter
        generator.generate_log("recaman", i_do_not_matter=True)


def catalan_log_missing_param(generator: SequenceGenerator) -> None:
    """
    A call to `SequenceGenerator.generate_log()` with known sequence key `seq_name` parameter,
    but missing other parameters should throw `MissingRequiredParameter`.
    This test also tests that parameters that are not required can be safely added, since the program ignores them.
    """
    with pytest.raises(MissingRequiredParameter):
        # Error: Missing 'first' parameter
        # Ignored: Supplied 'i_do_not_matter' parameter
        generator.generate_log("catalan", i_do_not_matter=True)


def range_up_log_missing_param(generator: SequenceGenerator) -> None:
    """
    A call to `SequenceGenerator.generate_log()` with known sequence key `seq_name` parameter,
    but missing other parameters should throw `MissingRequiredParameter`.
    This test also tests that parameters that are not required can be safely added, since the program ignores them.
    """
    with pytest.raises(MissingRequiredParameter):
        # Error: Missing 'first', 'step' parameter
        # Ignored: Supplied 'i_do_not_matter' parameter
        generator.generate_log("range_up", i_do_not_matter=True)


def range_down_log_missing_param(generator: SequenceGenerator) -> None:
    """
    A call to `SequenceGenerator.generate_log()` with known sequence key `seq_name` parameter,
    but missing other parameters should throw `MissingRequiredParameter`.
    This test also tests that parameters that are not required can be safely added, since the program ignores them.
    """
    with pytest.raises(MissingRequiredParameter):
        # Error: Missing 'first', 'step' parameter
        # Ignored: Supplied 'i_do_not_matter' parameter
        generator.generate_log("range_down", i_do_not_matter=True)


def long_dependency_log_missing_param(generator: SequenceGenerator) -> None:
    """
    A call to `SequenceGenerator.generate_log()` with known sequence key `seq_name` parameter,
    but missing other parameters should throw `MissingRequiredParameter`.
    This test also tests that parameters that are not required can be safely added, since the program ignores them.
    """
    with pytest.raises(MissingRequiredParameter):
        # Error: Missing 'first', 'second', 'third', 'fourth', 'fifth' parameter
        # Ignored: Supplied 'i_do_not_matter' parameter
        generator.generate_log("long_term_dependency", i_do_not_matter=True)


# Correct generate_log calls
def fib_log(generator: SequenceGenerator) -> None:
    """
    A call to `SequenceGenerator.generate_log()` with known sequence key `seq_name` parameter,
    and required other parameters for the `fib` sequence generator. As opposed to generate_trace, log produces sets of tuples (due to hashing). Test case is the default sequence list, which is the first (and only) element in the set.
    """
    expected = tuple(FIB[0 : generator.length])
    result = generator.generate_log("fib", firsts=[1], seconds=[1]).pop()
    assert_equal(expected, result)


def pascal_log(generator: SequenceGenerator) -> None:
    """
    A call to `SequenceGenerator.generate_log()` with known sequence key `seq_name` parameter,
    and required other parameters for the `pascal` sequence generator. As opposed to generate_trace, log produces sets of tuples (due to hashing). Test case is the default sequence list, which is the first (and only) element in the set.
    """
    expected = tuple(PASCAL[0 : generator.length])
    result = list(generator.generate_log("pascal", firsts=[1])).pop()
    assert_equal(expected, result)


def recaman_log(generator: SequenceGenerator) -> None:
    """
    A call to `SequenceGenerator.generate_log()` with known sequence key `seq_name` parameter,
    and required other parameters for the `recaman` sequence generator. As opposed to generate_trace, log produces sets of tuples (due to hashing). Test case is the default sequence list, which is the first (and only) element in the set.
    """
    expected = tuple(RECAMAN[0 : generator.length])
    result = list(generator.generate_log("recaman", firsts=[0])).pop()
    assert_equal(expected, result)


def catalan_log(generator: SequenceGenerator) -> None:
    """
    A call to `SequenceGenerator.generate_log()` with known sequence key `seq_name` parameter,
    and required other parameters for the `catalan` sequence generator. As opposed to generate_trace, log produces sets of tuples (due to hashing). Test case is the default sequence list, which is the first (and only) element in the set.
    """
    expected = tuple(CATALAN[0 : generator.length])
    result = list(generator.generate_log("catalan", firsts=[1])).pop()
    assert_equal(expected, result)


def range_up_log(generator: SequenceGenerator) -> None:
    """
    A call to `SequenceGenerator.generate_log()` with known sequence key `seq_name` parameter,
    and required other parameters for the `range_up` sequence generator. As opposed to generate_trace, log produces sets of tuples (due to hashing). Test case is the default sequence list, which is the first (and only) element in the set.
    """
    expected = tuple(UP[0 : generator.length])
    result = generator.generate_log("range_up", firsts=[1], steps=[1]).pop()
    assert_equal(expected, result)


def range_down_log(generator: SequenceGenerator) -> None:
    """
    A call to `SequenceGenerator.generate_log()` with known sequence key `seq_name` parameter,
    and required other parameters for the `range_down` sequence generator. As opposed to generate_trace, log produces sets of tuples (due to hashing). Test case is the default sequence list, which is the first (and only) element in the set.
    """
    expected = tuple(DOWN[-generator.length :])
    result = generator.generate_log("range_down", lasts=[1], steps=[1]).pop()
    assert_equal(expected, result)


def long_dependency_log(generator: SequenceGenerator) -> None:
    """
    A call to `SequenceGenerator.generate_log()` with known sequence key `seq_name` parameter,
    and required other parameters for the `long_term_dependency` sequence generator. As opposed to generate_trace, log produces sets of tuples (due to hashing). Test case is the default sequence list, which is the first (and only) element in the set.
    """
    expected = tuple(LONGTERM[0 : generator.length])
    result = generator.generate_log(
        "long_term_dependency",
        firsts=[1],
        seconds=[2],
        thirds=[3],
        fourths=[4],
        fifths=[5],
    ).pop()

    assert_equal(expected, result)


def fib_log_multiple_items_error(generator: SequenceGenerator) -> None:
    """
    A call to `SequenceGenerator.generate_log()` with known sequence key `seq_name` parameter,
    and required other parameters for the `fib` sequence generator. Tests that an exception is thrown: Since fib requires AT LEAST 2 parameters, we CANNOT generate lists of length 1.
    """
    if generator.length < 2:
        with pytest.raises(InvalidLengthException):
            generator.generate_log("fib", firsts=[1, 2, 3], seconds=[1, 2, 3, 4])


def fib_log_multiple_items(generator: SequenceGenerator) -> None:
    """
    A call to `SequenceGenerator.generate_log()` with known sequence key `seq_name` parameter,
    and required other parameters for the `fib` sequence generator. Tests that the correct number of traces are generated. Since fib requires AT LEAST 2 parameters, we CANNOT generate lists of length 1.
    """
    if generator.length < 2:
        with pytest.raises(InvalidLengthException):
            generator.generate_log("fib", firsts=[1, 2, 3], seconds=[1, 2, 3, 4])
    else:
        expected_traces_in_set = 12  # len(firsts) = 3 x len(seconds) = 4
        result = generator.generate_log("fib", firsts=[1, 2, 3], seconds=[1, 2, 3, 4])
        resulting_traces_in_set = len(result)
        assert_equal(expected=expected_traces_in_set, result=resulting_traces_in_set)


def pascal_log_multiple_items(generator: SequenceGenerator) -> None:
    """
    A call to `SequenceGenerator.generate_log()` with known sequence key `seq_name` parameter,
    and required other parameters for the `pascal` sequence generator. Tests that the correct number of traces are generated.
    """
    expected_traces_in_set = 3  # len(firsts) = 3
    result = generator.generate_log("pascal", firsts=[1, 2, 3])
    resulting_traces_in_set = len(result)
    assert_equal(expected=expected_traces_in_set, result=resulting_traces_in_set)


def recaman_log_multiple_items(generator: SequenceGenerator) -> None:
    """
    A call to `SequenceGenerator.generate_log()` with known sequence key `seq_name` parameter,
    and required other parameters for the `recaman` sequence generator. Tests that the correct number of traces are generated.
    """
    expected_traces_in_set = 3  # len(firsts) = 3
    result = generator.generate_log("recaman", firsts=[1, 2, 3])
    resulting_traces_in_set = len(result)
    assert_equal(expected=expected_traces_in_set, result=resulting_traces_in_set)


def catalan_log_multiple_items(generator: SequenceGenerator) -> None:
    """
    A call to `SequenceGenerator.generate_log()` with known sequence key `seq_name` parameter,
    and required other parameters for the `catalan` sequence generator. Tests that the correct number of traces are generated.
    """
    expected_traces_in_set = 3  # len(firsts) = 3
    result = generator.generate_log("catalan", firsts=[1, 2, 3])
    resulting_traces_in_set = len(result)
    assert_equal(expected=expected_traces_in_set, result=resulting_traces_in_set)


def range_up_log_multiple_items(generator: SequenceGenerator) -> None:
    expected_traces_in_set = 12  # len(firsts) = 3 x len(steps) = 4
    result = generator.generate_log("range_up", firsts=[1, 2, 3], steps=[1, 2, 3, 4])
    resulting_traces_in_set = len(result)
    assert_equal(expected=expected_traces_in_set, result=resulting_traces_in_set)


def range_down_log_multiple_items(generator: SequenceGenerator) -> None:
    expected_traces_in_set = 12  # len(lasts) = 3 x len(steps) = 4
    result = generator.generate_log("range_down", lasts=[3, 2, 1], steps=[4, 3, 2, 1])
    resulting_traces_in_set = len(result)
    assert_equal(expected=expected_traces_in_set, result=resulting_traces_in_set)


def long_dependency_log_multiple_items(generator: SequenceGenerator) -> None:
    # 5 x 2 x 3 x 1 x 4
    expected_traces_in_set = 120
    result = generator.generate_log(
        "long_term_dependency",
        firsts=[1, 2, 3, 4, 5],  # 5
        seconds=[1, 2],  # 2
        thirds=[2, 4, 5],  # 3
        fourths=[5],  # 1
        fifths=[1, 2, 3, 4],  # 4
    )

    resulting_traces_in_set = len(result)
    assert_equal(expected=expected_traces_in_set, result=resulting_traces_in_set)


def long_dependency_log_multiple_items_error(generator: SequenceGenerator) -> None:
    """
    A call to `SequenceGenerator.generate_log()` with known sequence key `seq_name` parameter,
    and required other parameters for the `long_term_dependency` sequence generator.
    Tests that an exception is thrown: Since long_term_dependency requires AT LEAST 5 parameters,
    we CANNOT generate lists of length 1, 2, 3, or 4.
    """
    if generator.length < 5:
        with pytest.raises(InvalidLengthException):
            generator.generate_log(
                "long_term_dependency",
                firsts=[1, 2, 3],
                seconds=[1, 2, 3, 4],
                thirds=[1, 2, 3, 4, 5],
                fourths=[1, 2, 3, 4, 5],
                fifths=[1, 2, 3, 4, 5],
            )


# Test initialisation exceptions
def test_exceptions() -> None:
    """
    Tests exceptions that should be raised when initialising the generator with incorrect values.
    See individual methods.
    """
    negative_length_should_raise_test()
    zero_length_should_raise_test()


# Test generate_trace
def test_generate_trace() -> None:
    """
    Tests `SequenceGenerator.generate_trace` for various inputs.
    See individual methods.
    """
    # Create some generator with default length
    generator = SequenceGenerator()

    # Errors
    nonexistent_trace(generator=generator)
    fib_trace_missing_param(generator=generator)
    pascal_trace_missing_param(generator=generator)
    recaman_trace_missing_param(generator=generator)
    catalan_trace_missing_param(generator=generator)
    range_up_missing_param(generator=generator)
    range_down_missing_param(generator=generator)
    long_dependency_missing_param(generator=generator)

    # Normal operation, various lengths
    generators = [
        SequenceGenerator(wanted_length=length) for length in [1, 5, 10, 50, 100]
    ]
    for generator in generators:
        fib_trace(generator=generator)
        pascal_trace(generator=generator)
        recaman_trace(generator=generator)
        catalan_trace(generator=generator)
        range_up_trace(generator=generator)
        range_down_trace(generator=generator)
        long_dependency_trace(generator=generator)


# Test generate_log
def test_generate_log() -> None:
    """
    Tests `SequenceGenerator.generate_log` for various inputs.
    See individual methods.
    """
    # Create some generator with default length
    generator = SequenceGenerator()

    # Errors
    nonexistent_log(generator=generator)
    fib_log_missing_param(generator=generator)
    pascal_log_missing_param(generator=generator)
    recaman_log_missing_param(generator=generator)
    catalan_log_missing_param(generator=generator)
    range_up_log_missing_param(generator=generator)
    range_down_log_missing_param(generator=generator)
    long_dependency_log_missing_param(generator=generator)

    # Fib wants 1+ param
    generator = SequenceGenerator(wanted_length=1)
    fib_log_multiple_items_error(generator=generator)

    # Long term wants 5+ params
    generators = [SequenceGenerator(wanted_length=length) for length in [1, 2, 3, 4]]
    for generator in generators:
        long_dependency_log_multiple_items_error(generator=generator)

    # Normal operation, various lengths
    generators = [SequenceGenerator(wanted_length=length) for length in [10, 50, 100]]
    for generator in generators:
        fib_log(generator=generator)
        pascal_log(generator=generator)
        recaman_log(generator=generator)
        catalan_log(generator=generator)
        range_up_log(generator=generator)
        range_down_log(generator=generator)
        long_dependency_log(generator=generator)

        # Note: wanted_length < required number of params should not be possible to call
        fib_log_multiple_items(generator=generator)
        pascal_log_multiple_items(generator=generator)
        recaman_log_multiple_items(generator=generator)
        catalan_log_multiple_items(generator=generator)
        range_up_log_multiple_items(generator=generator)
        range_down_log_multiple_items(generator=generator)
        long_dependency_log_multiple_items(generator=generator)
