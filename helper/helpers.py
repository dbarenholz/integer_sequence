from typing import Any, Dict, List

def check_item_list(item: Any, lst: List[Any]):
    """
    Raises a ``ValueError`` if a particular ``item`` is NOT contained in a particular ``lst``.

    :param Any item: The item to check for.
    :param List[Any] lst: The list to check in.
    :raises ValueError: if ``item`` not in ``lst``
    """
    if item not in lst:
        raise ValueError(f"There is no '{item}' in '{lst}'.")

def check_key_dict(key: Any, dictionary: Dict[Any, Any]):
    """
    Raises a ``ValueError`` if a particular ``key`` is NOT contained in a particular ``dictionary``.
    
    :param Any key: The key to check for.
    :param Dict[Any, Any] dictionary: The dictionary to check in.
    :raises ValueError: if ``key`` not in ``dictionary.keys()``
    """
    if key not in dictionary.keys():
        raise ValueError(f"There is no '{key}' in '{dictionary}'.")