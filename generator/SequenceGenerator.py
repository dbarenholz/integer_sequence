from typing import Any, Callable, Dict, Iterable, List, Optional, Set, Tuple, Union
import itertools

from helper import helpers


class SequenceGenerator:
    """
    Generates a sequence.
    """

    # Class Methods
    def __init__(self, wanted_length: int = 10):
        """
        Initializes a sequence generator that generates sequences of length ``self.length``.

        Creates a ```self.config`` dictionary that holds information on implemented methods.
        """
        self.length: int = wanted_length
        self.config: Dict[
            str, Dict[str, Union[List[str], Callable[[Optional[int]], Iterable[int]]]]
        ] = {
            "fib": {"parameters": ["first", "second"], "method": self.fib_wrapper},
            "pascal": {"parameters": ["base_number"], "method": self.pascal_wrapper},
        }

    def __repr__(self):
        return f"SequenceGenerator(length={self.length}, implemented_generators={self.get_generators()})"

    # Generator methods
    def fib(self, first: int, second: int) -> Iterable[int]:
        """
        Yield the first ``self.length`` numbers of the Fibonnaci sequence where the first term is ``first`` and the second term is `second`.

        :param int first: The first element of the sequence.
        :param int second: The second element of the sequence.
        :return A generator that generates the sequence.
        :rtype Iterable[int]
        """
        # Handle errorenous length
        if self.length < 0:
            raise Exception("Cannot create negative length list.")
        # Empty case, no yields
        if self.length == 0:
            return
        # If for some reason you only want the first number?
        if self.length == 1:
            yield first
            return
        # Normal case: yield the first 2 numbers, then loop
        yield first
        yield second

        # Keep track of a count
        count = 0
        while count < self.length - 2:
            # Increment the count
            count += 1
            # Compute the current fib number as sum of the previous two
            current = first + second
            # yield it
            yield current
            # update values
            first = second
            second = current

    def fib_wrapper(self, params: Dict[str, int]) -> Iterable[int]:
        """
        Wrapper method for ``self.fib``. Written so we can have a unified interface to generate traces, given a sequence key.

        Unsafe, when used in any other place than the generation config dict.
        """
        return self.fib(params["first"], params["second"])

    def pascal(self, base_number: int) -> Iterable[int]:
        """
        Yield the first ``self.length`` numbers of the sequence defined by reading the pascal triangle from left to right, top to bottom, where the first integer is ``base_number`` (usually this is 1).

        :param int base_number: The first integer on top of the triangle, and consequently the first integer in the sequence.
        :return A generator that generates the sequence.
        :rtype Iterable[int]
        """
        # Handle errorenous length
        if self.length < 0:
            raise Exception("Cannot create negative length list.")
        # Empty case, no yields
        if self.length == 0:
            return
        # If for some reason you only want the first number?
        if self.length == 1:
            yield base_number
            return

        def next_row(row):
            tmp = 0
            for val in row:
                yield tmp + val
                tmp = val
            yield base_number

        row = [base_number]
        # We are interested in only the items, not lists
        for item in row:
            yield item

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

    def pascal_wrapper(self, params: Dict[str, int]) -> Iterable[int]:
        """
        Wrapper method for ``self.pascal``. Written so we can have a unified interface to generate traces, given a sequence key.

        Unsafe, when used in any other place than the generation config dict.
        """
        return self.pascal(params["base_number"])

    # Private getters
    def __get_params(self, seq_name: str) -> List[str]:
        """
        Getter for config parameters.
        """
        return self.config[seq_name]["parameters"]

    def __get_method(self, seq_name: str) -> Callable[[Optional[int]], Iterable[int]]:
        """
        Getter for config method.
        """
        return self.config[seq_name]["method"]

    # Public getters
    def get_generators(self) -> List[str]:
        """
        Getter for implemented generator functions
        """
        return [generator for generator in self.config.keys()]

    # Private methods
    def __check_params(self, given: List[str], required: List[str]) -> None:
        """
        Checks whether or not supplied parameters to ``self.generate_trace`` or ``self.generate_log`` coincide with required parameters.
        Raises a ``ValueError`` when something that was required wasn't there.
        """
        for param in required:
            if param not in given:
                raise ValueError(f"Required parameter '{param}' was not present.")

    def __build_params(self, given: List[Any], required: List[Any]) -> Dict[str, Any]:
        """
        Builds a keyword-argument dictionary given the parameters in ``self.generate_trace`` or ``self.generate_log``.

        Returns a dictionary of the form:
        {
            "param1" : value,
            "param2" : value,
            ...
        }
        """
        return {
            required_parameter: given[required_parameter]
            for required_parameter in required
        }

    def __build_param_matrix(
        self, givens: List[List[Any]], requireds: List[List[Any]]
    ) -> List[Dict[str, int]]:
        """
        Builds parameter list for usage in ``self.generate_log``. Essentially this method transforms a dictionary ``array_dict``:

        {
            "required_param1" : [1, 2, ..],
            "required_param2" : [1, 2, 3, 4, ..],
            "required_param3" : [1, ..],
            ..
        }

        to our wanted list:

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

    # Public methods
    def generate_trace(self, seq_name: str, **params) -> Iterable[int]:
        """
        Generates a single trace corresponding to some sequence.
        """
        helpers.check_item_list(seq_name.strip().lower(), self.get_generators())

        # It exists, check for param mismatch
        required_params = self.__get_params(seq_name)
        self.__check_params(params, required_params)

        # required (and possibly more) params present -- retrieve reference to generator
        method = self.__get_method(seq_name)

        # build params to pass through
        method_params = self.__build_params(params, required_params)

        # call the function, and return its result
        return method(method_params)

    def generate_log(self, seq_name: str, **params) -> Set[Tuple[int]]:
        """
        Generates a single trace corresponding to some sequence.
        """
        helpers.check_item_list(seq_name.strip().lower(), self.get_generators())

        required_params = [param + "s" for param in self.__get_params(seq_name)]
        self.__check_params(params, required_params)

        # Create the log variable as a set
        log = set()

        for params in self.__build_param_matrix(params, required_params):
            trace = tuple(self.generate_trace(seq_name, **params))
            log.add(trace)

        return log
