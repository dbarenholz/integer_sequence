# Typing
from typing import Dict, List, Tuple

# Python Packages
from os import access, R_OK
from os.path import isfile
from xml.etree import ElementTree as ET
import gzip

# Own
from exception import UnsupportedOrInvalidLogFormat, InvalidElementPassed


class XESTransformator:
    """
    Transforms a process mining log into integer sequences.
    Can only handle extensions present in `readable_exts`.

    Attributes:
      readable_exts -- All extensions that this transformator can handle.
    """

    # Class Methods
    def __init__(self) -> None:
        """
        Initialises the XESTransformator class.
        """
        self.readable_exts = [".xes", ".xes.gz"]
        """All extensions that this transformator can handle."""

    def __repr__(self) -> str:
        return f"XESTransformator(readable_exts={self.readable_exts})"

    # Helper methods
    def __check_log(self, file: str) -> None:
        """
        Performs some checks on the file and
        raises exceptions when something is wrong.

        In particular:
        Check 0: Check if it is a file.
        Check 1: Check if the file is readable.
        Check 2: Check if the extension is one that we can parse.

        Parameters:
          file -- The file (as string) to check. Can be relative or absolute path.

        Raises `FileNotFoundError` if check 0 fails.
        Raises `PermissionError` if check 1 fails.
        Raises `UnsupportedOrInvalidLogFormat` if check 2 fails.
        """
        # Check 0: Did we get a file?
        if not isfile(file):
            raise FileNotFoundError(file)

        # Check 1: Can we read the file?
        if not access(file, R_OK):
            raise PermissionError(file)

        # Check 2: Is the extension in one of the readable ones?
        if not any([True for ext in self.readable_exts if ext in file]):
            raise UnsupportedOrInvalidLogFormat(filepath=file)

    def __build_mapping(self, root: ET.Element) -> Dict[str, int]:
        """
        Builds a mapping from key (XES concept:name) to integer.

        Parameters:
          root -- The root element (`<log>`) of an XES log file.

        Returns a dictionary mapping a string (key) to an integer.
        """
        # Check element tag
        if "log" not in root.tag:
            raise InvalidElementPassed(expected="log", element=root.tag)

        # Retrieve element by XPath
        dictionary_root_field = root.find(
            ".//*[@key='meta_concept:named_events_total']"
        )

        if dictionary_root_field is None:
            raise UnsupportedOrInvalidLogFormat(
                filepath="N/A", message="Error while building mapping."
            )

        # Initialise the mapping as empty dictionary
        mapping = dict()

        # Loop through all elements
        for index, element in enumerate(dictionary_root_field.iter()):
            # Skip the root item itself.
            if element != dictionary_root_field:
                # Retrieve the key from element attributes
                key = element.attrib["key"]

                # Set the mapping entry to an integer (index is used)
                mapping[key] = index

        return mapping

    def __get_all_traces(self, root: ET.Element) -> List[ET.Element]:
        """
        Given the root element (should be log), return a list of all trace elements.

        Parameters:
          root -- The root element (`<log>`) of an XES log file.

        Returns a list of trace elements (`<trace>`).
        """
        if "log" not in root.tag:
            raise InvalidElementPassed(expected="log", element=root.tag)

        return [elem for elem in root.iter() if "trace" in elem.tag]

    def __get_all_events(self, root: ET.Element) -> List[ET.Element]:
        """
        Given the root element (should be trace), return a list of all event elements.

        Parameters:
          root -- Any trace element (`<trace>`) of an XES log file.

        Returns a list of event elements (`<event>`).
        """
        if "trace" not in root.tag:
            raise InvalidElementPassed(expected="trace", element=root.tag)

        return [elem for elem in root.iter() if "event" in elem.tag]

    # Parsing methods
    def __parse_with_ET(self, file: str, gzipped: bool = False) -> ET.ElementTree:
        """
        Parse the XML with ElementTree
        Distinguishes between gzipped and normal format.

        Parameters:
          file -- The file to parse.
          gzipped -- Boolean indicating whether or not the file is gzipped.
                     False by default.
        """
        if gzipped:
            with gzip.open(file) as unzipped_file:
                return ET.parse(unzipped_file)
        return ET.parse(file)

    def __parse(self, file: str) -> ET.Element:
        """
        Parses a file (that is either .xes or .xes.gz) with ElementTree and returns the root element.

        Parameters:
          file -- The file to parse.

        Returns the root element (`<log>`) of an XES log.
        """
        tree = self.__parse_with_ET(file, ".gz" in file)
        return tree.getroot()

    # Transforming methods
    def __convert_trace(
        self, trace: ET.Element, mapping: Dict[str, int]
    ) -> Tuple[int, ...]:
        """
        Converts a single trace element into a tuple of integers.

        Parameters:
          trace -- The trace element (`<trace>`) to convert.
          mapping -- The mapping that defines how to convert.

        Returns a tuple of integers representing a trace according to some mapping.
        """

        # Check element tag
        if "trace" not in trace.tag:
            raise InvalidElementPassed(expected="trace", element=trace.tag)

        converted = []
        for event in self.__get_all_events(trace):
            key_element = event.find(".//*[@key='concept:name']")
            if key_element:
                key_itself = key_element.attrib["value"]
                converted.append(mapping[key_itself])
            else:
                # Got None, cannot process this file.
                raise UnsupportedOrInvalidLogFormat(
                    filepath="N/A", message="Error while converting a trace."
                )

        return tuple(converted)

    def __make_log(
        self, root: ET.Element, mapping: Dict[str, int]
    ) -> List[Tuple[int, ...]]:
        """
        Makes a log, given a root element and a mapping dictionary.

        Parameters:
          root -- the root element (`<log>`) of an XES log.
          mapping -- a mapping from key (XES concept:name) to integer.

        Returns a transformed log.
        """

        # Check element tag
        if "log" not in root.tag:
            raise InvalidElementPassed(expected="log", element=root.tag)

        # Initialise empty log list
        log = []

        # Iterate over all traces
        for trace in self.__get_all_traces(root):
            # Convert a single trace and add it to the log
            converted_trace = self.__convert_trace(trace, mapping)
            log.append(converted_trace)

        return log

    def transform(self, log: str) -> List[Tuple[int, ...]]:
        """
        Transforms a XES log into integer sequences.

        Parameters:
          log -- A logfile to transform to integer sequences.

        Returnsa transformed log.
        """
        # Check the log
        self.__check_log(log)

        # Parse the log if possible
        root = self.__parse(log)

        # Build the name mapping
        name_mapping = self.__build_mapping(root)

        # Build the log
        return self.__make_log(root, name_mapping)
