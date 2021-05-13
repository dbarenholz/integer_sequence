# Typing
from typing import Any, Callable, Dict, Generator, List, Tuple

# Packages
import itertools

# Own
from exception import (
    InvalidLengthException,
    MissingRequiredParameter,
    MissingItem,
    NotYetImplemented,
)
from helper import check_item_list


class SequenceGenerator:
    """
    Generates a log of traces that originate from the same generating distribution / method.

    Attributes:
      length -- The amount of items to generate.
      config -- A config object that holds, per implemented metod,
                a list of required parameters and a reference to the method.
    """

    # Class Methods
    def __init__(self, wanted_length: int = 10):
        """
        Initializes the SequenceGenerator class.

        Parameters:
          wanted_length -- The desired amount of items to generate.
                           10 by default.
        """
        # Test for invalid lengths
        if wanted_length <= 0:
            raise InvalidLengthException(wanted_length)

        # At this point we know that length is at least 1.
        self.length: int = wanted_length
        """The amount of items to generate."""
        self.config: Dict[str, Dict[str, Any]] = {
            "fib": {"parameters": ["first", "second"], "method": self.__fib_wrapper},
            "pascal": {"parameters": ["first"], "method": self.__pascal_wrapper},
            "recaman": {"parameters": ["first"], "method": self.__recaman_wrapper},
            "catalan": {"parameters": ["first"], "method": self.__catalan_wrapper},
        }
        """A config object that holds, per implemented metod,
        a list of required parameters and a reference to the method."""

    def __repr__(self) -> str:
        return f"SequenceGenerator(length={self.length}, implemented_generators={self.get_generators()})"

    # Generator methods
    def __fib(self, first: int = 1, second: int = 1) -> Generator:
        """
        Yield the first `self.length` numbers of the Fibonnaci sequence
        where the first term is `first` and the second term is `second`.

        Parameters:
          first -- The first element of the sequence.
          second -- The second element of the sequence.

        Returns a generator that generates the sequence.
        """
        yield first
        # If you only want 1 number, for some reason?
        if self.length == 1:
            return

        yield second

        count = 0
        while count < self.length - 2:
            # Increment count
            count += 1
            # Compute next value
            current = first + second
            yield current
            # Update values
            first = second
            second = current

    def __fib_wrapper(self, params: Dict[str, int]) -> Generator:
        """
        Wrapper method for `self.fib`.
        Written so we can have a unified interface to generate traces, given a sequence key.

        **Unsafe** when used in any other place than the generation config dict `SequenceGenerator.config`.
        """
        return self.__fib(first=params["first"], second=params["second"])

    def __pascal(self, first: int = 1) -> Generator:
        """
        Yield the first `self.length` numbers of the sequence defined by
        reading the pascal triangle from left to right, top to bottom,
        where the first integer is `first` (usually this is 1).

        Parameters:
          first -- The first integer on top of the triangle,
                   and consequently the first integer in the sequence.

        Returns a generator that generates the sequence.
        """
        yield first

        # If for some reason you only want the first number?
        if self.length == 1:
            return

        def next_row(row: List[int]) -> Generator:
            """
            Computes the next row in the triangle of pascal.

            Parameters:
              row -- The current row.

            Returns a generator yielding elements of the next row.
            """
            tmp = 0
            for val in row:
                yield tmp + val
                tmp = val
            yield first

        row = [first]
        # Keep track of counts, start at 1
        counts = 1

        while True:
            # compute the next row
            next = list(next_row(row))

            # loop through them
            for item in next:
                # test for length
                if counts < self.length:
                    yield item
                    counts += 1
                else:
                    return

            row = next

    def __pascal_wrapper(self, params: Dict[str, int]) -> Generator:
        """
        Wrapper method for `self.pascal`.
        Written so we can have a unified interface to generate traces, given a sequence key.

        **Unsafe** when used in any other place than the generation config dict `SequenceGenerator.config`.
        """
        return self.__pascal(first=params["first"])

    def __recaman(self, first: int = 0) -> Generator:
        """
        Generator for the Recaman's sequence, a well known sequence
        from the on-line encyclopedia of integer sequences.
        Available [here](https://oeis.org/A005132).

        Parameters:
          first -- The first element of the sequence.
                   The original sequence defines this as 0.

        Returns a generator that generates the sequence.
        """
        # If for some reason you only want the first number?
        if self.length == 1:
            yield first
            return

        # Keep track of a count and already seen digits
        count = 0
        current = first
        already_seen = set([])

        def get_next(current: int, index: int) -> int:
            """
            Computes the next value in the sequence.

            Parameters:
              current -- The current value.
              index -- The index of the current value.

            Returns the new value.
            """
            # Compute a(n) = a(n-1) - n
            # if nonnegative and not in sequence, return
            new_number = current - index

            if (new_number < 0) | (new_number in already_seen):
                # Negative or already seen: add index in stead
                new_number = current + index

            return new_number

        while count < self.length:
            # Compute next term in the sequence
            new = get_next(current, count)

            # Save it to the set of already seen terms
            already_seen.add(new)

            # Set current to new value and increase count
            count += 1
            current = new

            # Finally, yield the correct value
            yield current

    def __recaman_wrapper(self, params: Dict[str, int]) -> Generator:
        """
        Wrapper method for `self.recaman`.
        Written so we can have a unified interface to generate traces, given a sequence key.

        **Unsafe** when used in any other place than the generation config dict `SequenceGenerator.config`.
        """
        return self.__recaman(first=params["first"])

    def __catalan(self, first: int = 1) -> Generator:
        """
        Generates the Catalan numbers, where the first integer is parametrised.
        The catalan sequence is available [here](https://oeis.org/A000108).

        Implemented using dynamic programming as the direct formula has issues with `n > 30`
        In particular, 14544636039226909 became 14544636039226908 and all subsequent values were off.

        Parameters:
          first -- The first element of the sequence.
                   The original sequence defines this as 1.

        Returns a generator that generates the sequence.
        """
        # Initialise dynamic programming table
        dp = [0] * (self.length + 1)
        dp[0] = first  # in our case this is a parameter. By default it should be 1.
        dp[1] = first  # in our case this is a parameter. By default it should be 1.

        # Fill the dp entries based on the recursive formula
        for i in range(2, self.length + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]

        # Loop through table, and yield the next item as long as the index does not exceed the length!
        for index in range(len(dp)):
            if index < self.length:
                yield dp[index]

    def __catalan_wrapper(self, params: Dict[str, int]) -> Generator:
        """
        Wrapper method for `self.recaman`.
        Written so we can have a unified interface to generate traces, given a sequence key.

        **Unsafe** when used in any other place than the generation config dict `SequenceGenerator.config`.
        """
        return self.__catalan(first=params["first"])

    # Private getters
    def __get_params(self, seq_name: str) -> List[str]:
        """
        Gets config parameters for a particul sequence generator.

        Parameters:
          seq_name -- The name of the sequence generation method for which to retrieve parameters.

        Returns a list of parameters.
        """
        params = [str(item) for item in self.config[seq_name]["parameters"]]
        return params

    def __get_method(self, seq_name: str) -> Callable[[Dict[str, int]], Generator]:
        """
        Gets the method reference for a particular sequence generator.

        Parameters:
          seq_name -- The name of the sequence generation method for which to retrieve a method reference.

        Returns a method reference.
        """
        return self.config[seq_name]["method"]

    # Helper methods
    def __check_params(self, given: Dict[str, Any], required: List[str]) -> None:
        """
        Checks correctness of supplied parameters to `self.generate_trace` or `self.generate_log`.

        Parameters:
          given -- The given dictionary.
          required  -- The required items.

        Raises a ``MissingRequiredParameter`` when something that was required wasn't there.
        """
        missing = [param for param in required if param not in given]
        if missing:
            raise MissingRequiredParameter(missing)

    def __build_params(
        self, given: Dict[str, Any], required: List[Any]
    ) -> Dict[str, Any]:
        """
        Builds a keyword-argument dictionary given the parameters in `self.generate_trace` or `self.generate_log`.

        Parameters:
          given -- The given dictionary.
          required  -- The required items.

        Returns a dictionary of the form:
        ```
        {
            "param1" : value,
            "param2" : value,
            ...
        }
        ```
        """
        return {
            required_parameter: given[required_parameter]
            for required_parameter in required
        }

    def __build_param_matrix(
        self, givens: Dict[str, Any], requireds: List[str]
    ) -> List[Dict[str, int]]:
        """
        Builds parameter list for usage in `self.generate_log`.

        Transforms a dictionary of shape:
        ```
        {
            "required_param1" : [1, 2, ..],
            "required_param2" : [1, 2, 3, 4, ..],
            "required_param3" : [1, ..],
            ..
        }
        ```
        to our wanted list of shape:
        ```
        [
            {
                "required_param1" : 1,
                "required_param2" : 1,
                "required_param3" : 1
            },
            ...
            {
                "required_param1" : 3,
                "required_param2" : 3,
                "required_param3" : 3
            }
        ]
        ```

        Parameters:
          given -- The given dictionary.
          required  -- The required items.

        Returns a list of dictionaries as listed above.
        """
        # Keep result variable
        result = []

        # Create dictionary out of lists
        array_dict = self.__build_params(givens, requireds)

        # Compute the cartesian product using itertools
        compute_product_of_me = list(array_dict.values())
        for tuple_of_vals in itertools.product(*compute_product_of_me):
            # tuple_of_vals: (a, b, c, ...)
            # len(item) == len(keys)
            # item[0] corresponds with keys[0]
            keys = [key[:-1] for key in array_dict.keys()]
            result.append({key: value for (key, value) in zip(keys, tuple_of_vals)})

        return result

    def __check_length_with_params(self, seq_name: str) -> None:
        """
        Checks whether or not we can mathematically generate a trace of length `self.length`
        given a particular generator, identified by `seq_name`.

        Parameters:
          seq_name -- The name of the sequence generation method for which to perform this check.

        Raises an `InvalidLengthException` when a sequence cannot be generated
        due to mismatch of required params and wanted length.
        """
        min_len_for_method = len(self.__get_params(seq_name))
        if min_len_for_method > self.length:
            raise InvalidLengthException(
                length=min_len_for_method,
                message=f"Cannot generate sequence of length {self.length}\
                    if a method needs a minimum of %s parameters",
            )

    # Public methods
    def get_generators(self) -> List[str]:
        """
        Gets implemented generator functions.

        Returns a list of the names of implemented generator functions.
        """
        return [generator for generator in self.config.keys()]

    def generate_trace(self, seq_name: str, **kwargs: Any) -> Generator:
        """
        Generates a single trace corresponding to some sequence.

        Parameters:
          seq_name -- The name of the sequence generation method for which to generate a trace.

        Raises a `NotYetImplemented` when the `seq_name` key does not correspond to a generator method.
        Raises a `MissingRequiredParameter` when a particular parameter was not provided.

        Returns a generator for a particular sequence.
        """
        try:
            check_item_list(seq_name.strip().lower(), self.get_generators())
        except MissingItem:
            raise NotYetImplemented(seq_name)

        # It exists, check for param mismatch
        required_params = self.__get_params(seq_name)
        self.__check_params(kwargs, required_params)

        # required (and possibly more) params present -- retrieve reference to generator
        method = self.__get_method(seq_name)

        # build params to pass through
        method_params = self.__build_params(kwargs, required_params)

        # call the function, and return its result
        return method(method_params)

    def generate_log(self, seq_name: str, **kwargs: Any) -> List[Tuple[int, ...]]:
        """
        Generates an entire log corresponding to some sequence.

        Parameters:
          seq_name -- The name of the sequence generation method for which to generate a log.

        Raises a `NotYetImplemented` when the `seq_name` key does not correspond to a generator method.
        Raises a `MissingRequiredParameter` when a particular parameter was not provided.

        Returns a log of traces a list of tuples.
        """
        try:
            check_item_list(seq_name.strip().lower(), self.get_generators())
        except MissingItem:
            raise NotYetImplemented(seq_name)

        required_params = [param + "s" for param in self.__get_params(seq_name)]
        self.__check_params(kwargs, required_params)
        self.__check_length_with_params(seq_name)

        # Create the log variable as a set
        log = []

        for params in self.__build_param_matrix(kwargs, required_params):
            trace = tuple(self.generate_trace(seq_name, **params))
            log.append(trace)

        return log
