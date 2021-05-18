# Typing
from typing import Any, Dict, List
from os import getcwd
from os.path import join
from pickle import dump, load

# Own
from exception import MissingItem


def check_item_list(item: Any, lst: List[Any]) -> None:
    """
    Raises a ``MissingItem`` if a particular ``item`` is NOT contained in a particular ``lst``.

    :param Any item: The item to check for.
    :param List[Any] lst: The list to check in.
    :raises MissingItem: if ``item`` not in ``lst``
    """
    if item not in lst:
        raise MissingItem(item, lst)


def check_key_dict(key: Any, dictionary: Dict[Any, Any]) -> None:
    """
    Raises a ``MissingItem`` if a particular ``key`` is NOT contained in a particular ``dictionary``.

    :param Any key: The key to check for.
    :param Dict[Any, Any] dictionary: The dictionary to check in.
    :raises MissingItem: if ``key`` not in ``dictionary.keys()``
    """
    if key not in dictionary.keys():
        raise MissingItem(key, dictionary)


def assert_equal(expected: Any, result: Any) -> None:
    """
    Asserts that expected is equal to result.
    To be called from tests.

    :param Any expected: The expected outcome of some function call.
    :param Any result: The resulted outcome of some function call.
    :raises AssertionError: when equality fails
    """
    assert expected == result


def dumps(filename: str, data: Any) -> bool:
    """
    Dumps data to a file using pickle.

    Returns true on success.
    Returns false on failure.
    """
    try:
        with open(f"{filename}.pkl", "wb") as file:
            dump(data, file)
        return True
    except OSError:
        return False


def loads(filename: str) -> Any:
    """
    Loads data from a file using pickle.
    """
    with open(f"{filename}.pkl", "rb") as pickle:
        return load(pickle)


# Paths
ROOTPATH = getcwd()
DATAPATH = join(ROOTPATH, "data")
LOGPATH = join(ROOTPATH, "logs")
TESTPATH = join(ROOTPATH, "test")
