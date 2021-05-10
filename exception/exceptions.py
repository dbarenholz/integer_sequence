# Typing
from typing import Any, Dict, List, Union


class InvalidLengthException(Exception):
    """
    Raised when a sequence generator was given an invalid length on initialisation,
    or when a length is smaller than the required number of parameters for a generator method.

    Attributes:
      length -- given length
    """

    def __init__(
        self,
        length: int = 0,
        message: str = "Attempted to create a sequence generator with invalid length: '%s'",
    ) -> None:
        self.length = length
        self.message = message % length
        super().__init__(self.message)

    def __repr__(self) -> str:
        return f"{self.length} -> {self.message}"


class NotYetImplemented(Exception):
    """
    Raised when a sequence generator was given a key for a sequence function that is not implemented.

    Attributes:
      key -- key pointing to no implementation
    """

    def __init__(
        self,
        key: str,
        message: str = "Attempted to call unimplemented method by key: '%s'",
    ) -> None:
        self.key = key
        self.message = message % key
        super().__init__(self.message)

    def __repr__(self) -> str:
        return f"{self.key} -> {self.message}"


class MissingRequiredParameter(Exception):
    """
    Raised when a sequence generator was given insufficient parameters to generate a sequence.

    Attributes:
      params -- required parameters that were not present
    """

    def __init__(
        self,
        params: List[str],
        message: str = "Attempted to call method without required parameters from '%s'",
    ) -> None:
        self.params = params
        self.message = message % params
        super().__init__(self.message)

    def __repr__(self) -> str:
        return f"{self.params} -> {self.message}"


class MissingItem(Exception):
    """
    Raised when an item (in a list or dictionary) was missing.

    Attributes:
      item -- required item that were not present
      container -- list or dictionary that was supposed to contain item
    """

    def __init__(
        self,
        item: Any,
        container: Union[List[Any], Dict[Any, Any]],
        message: str = "There is no %s in %s",
    ) -> None:
        self.item = item
        self.container = container
        self.message = message % (item, container)
        super().__init__(self.message)

    def __repr__(self) -> str:
        return f"{self.item}, {self.container} -> {self.message}"
