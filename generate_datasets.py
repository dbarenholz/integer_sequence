# ! /home/dan/miniconda3/bin/conda "run -n internship python"
# -*- coding: utf-8 -*-
from typing import List, Tuple, Dict
from os import listdir
from os.path import join


# Own
from generator import SequenceGenerator, XESTransformator
from helper import DATAPATH, dumps, LOGPATH


def transform() -> None:
    """
    Generates datasets by transforming XES logs.

    Raises an OSError when it could not succesfully save the generated log.
    """
    # Bad check for file name extension, but Transformator class checks properly
    TO_TRANSFORM = [file for file in listdir(DATAPATH) if ".xes" in file]

    transformator = XESTransformator()

    for to_transform in TO_TRANSFORM:
        print(f"Attempting to transform '{to_transform}' with '{transformator}'...")
        transformed = transformator.transform(join(DATAPATH, to_transform))
        success = dumps(join(LOGPATH, f"{to_transform}-transformed"), transformed)
        if not success:
            raise OSError("Failed to dump data to disk..")
        else:
            print("Success!")


def generate() -> None:
    """
    Generates datasets with sequence generators. Refer to `configurations_to_use` for all used generation configs.

    Raises an OSError when it could not succesfully save the generated log.
    """
    # Shorthand for a bunch of numbers to be used in configs below
    # Exclude 0 for multiplication issues
    some_numbers = list(range(1, 101))

    configurations_to_use: List[Tuple[str, str, Dict[str, List[int]]]] = [
        # Fib, fixed 0 first element, random seconds
        ("fib", "fixed0-random", {"firsts": [0], "seconds": some_numbers}),
        # Fib, fixed 0 second element, random firsts
        ("fib", "random-fixed0", {"firsts": some_numbers, "seconds": [0]}),
        # Fib, fixed 1 first element, random seconds
        ("fib", "fixed1-random", {"firsts": [1], "seconds": some_numbers}),
        # Fib, fixed 1 second element, random firsts
        ("fib", "random-fixed1", {"firsts": some_numbers, "seconds": [1]}),
        # Fib, generic, random all
        ("fib", "generic", {"firsts": some_numbers, "seconds": some_numbers}),
        # Pascal, no cases
        ("pascal", "", {"firsts": some_numbers}),
        # Recaman, no cases
        ("recaman", "", {"firsts": some_numbers}),
        # Catalan, no cases
        ("catalan", "", {"firsts": some_numbers}),
        # Counting up from various, identical step sizes
        # Generated and then unpacked
        *[
            ("range_up", f"step-{step}", {"firsts": some_numbers, "steps": [step]})
            for step in some_numbers
        ],
        # Counting down to various, identical step sizes
        # Generated and then unpacked
        *[
            ("range_down", f"step-{step}", {"lasts": some_numbers, "steps": [step]})
            for step in some_numbers
        ],
        # Various long term configs
        (
            "long_term_dependency",
            "firsts0",
            {
                "firsts": some_numbers,
                "seconds": [0],
                "thirds": [0],
                "fourths": [0],
                "fifths": [0],
            },
        ),
        (
            "long_term_dependency",
            "seconds0",
            {
                "firsts": [0],
                "seconds": some_numbers,
                "thirds": [0],
                "fourths": [0],
                "fifths": [0],
            },
        ),
        (
            "long_term_dependency",
            "thirds0",
            {
                "firsts": [0],
                "seconds": [0],
                "thirds": some_numbers,
                "fourths": [0],
                "fifths": [0],
            },
        ),
        (
            "long_term_dependency",
            "fourths0",
            {
                "firsts": [0],
                "seconds": [0],
                "thirds": [0],
                "fourths": some_numbers,
                "fifths": [0],
            },
        ),
        (
            "long_term_dependency",
            "fifths0",
            {
                "firsts": [0],
                "seconds": [0],
                "thirds": [0],
                "fourths": [0],
                "fifths": some_numbers,
            },
        ),
        (
            "long_term_dependency",
            "firsts1",
            {
                "firsts": some_numbers,
                "seconds": [1],
                "thirds": [1],
                "fourths": [1],
                "fifths": [1],
            },
        ),
        (
            "long_term_dependency",
            "seconds1",
            {
                "firsts": [1],
                "seconds": some_numbers,
                "thirds": [1],
                "fourths": [1],
                "fifths": [1],
            },
        ),
        (
            "long_term_dependency",
            "thirds1",
            {
                "firsts": [1],
                "seconds": [1],
                "thirds": some_numbers,
                "fourths": [1],
                "fifths": [1],
            },
        ),
        (
            "long_term_dependency",
            "fourths1",
            {
                "firsts": [1],
                "seconds": [1],
                "thirds": [1],
                "fourths": some_numbers,
                "fifths": [1],
            },
        ),
        (
            "long_term_dependency",
            "fifths1",
            {
                "firsts": [1],
                "seconds": [1],
                "thirds": [1],
                "fourths": [1],
                "fifths": some_numbers,
            },
        ),
        # Cannot go up to 100 - memory error on laptop (could have been expected)
        # In stead, go up to 10
        (
            "long_term_dependency",
            "generic",
            {
                "firsts": list(range(1, 11)),
                "seconds": list(range(1, 11)),
                "thirds": list(range(1, 11)),
                "fourths": list(range(1, 11)),
                "fifths": list(range(1, 11)),
            },
        ),
        # Various long term single dependency logs
        *[
            (
                "long_term_single_dependency",
                f"firsts0-const{const}",
                {
                    "firsts": some_numbers,
                    "seconds": [0],
                    "thirds": [0],
                    "fourths": [0],
                    "fifths": [0],
                    "constants": [const],
                },
            )
            for const in some_numbers
        ],
        *[
            (
                "long_term_single_dependency",
                f"seconds0-const{const}",
                {
                    "firsts": [0],
                    "seconds": some_numbers,
                    "thirds": [0],
                    "fourths": [0],
                    "fifths": [0],
                    "constants": [const],
                },
            )
            for const in some_numbers
        ],
        *[
            (
                "long_term_single_dependency",
                f"thirds0-const{const}",
                {
                    "firsts": [0],
                    "seconds": [0],
                    "thirds": some_numbers,
                    "fourths": [0],
                    "fifths": [0],
                    "constants": [const],
                },
            )
            for const in some_numbers
        ],
        *[
            (
                "long_term_single_dependency",
                f"fourths0-const{const}",
                {
                    "firsts": [0],
                    "seconds": [0],
                    "thirds": [0],
                    "fourths": some_numbers,
                    "fifths": [0],
                    "constants": [const],
                },
            )
            for const in some_numbers
        ],
        *[
            (
                "long_term_single_dependency",
                f"fifths0-const{const}",
                {
                    "firsts": [0],
                    "seconds": [0],
                    "thirds": [0],
                    "fourths": [0],
                    "fifths": some_numbers,
                    "constants": [const],
                },
            )
            for const in some_numbers
        ],
        *[
            (
                "long_term_single_dependency",
                f"firsts1-const{const}",
                {
                    "firsts": some_numbers,
                    "seconds": [1],
                    "thirds": [1],
                    "fourths": [1],
                    "fifths": [1],
                    "constants": [const],
                },
            )
            for const in some_numbers
        ],
        *[
            (
                "long_term_single_dependency",
                f"seconds1-const{const}",
                {
                    "firsts": [1],
                    "seconds": some_numbers,
                    "thirds": [1],
                    "fourths": [1],
                    "fifths": [1],
                    "constants": [const],
                },
            )
            for const in some_numbers
        ],
        *[
            (
                "long_term_single_dependency",
                f"thirds1-const{const}",
                {
                    "firsts": [1],
                    "seconds": [1],
                    "thirds": some_numbers,
                    "fourths": [1],
                    "fifths": [1],
                    "constants": [const],
                },
            )
            for const in some_numbers
        ],
        *[
            (
                "long_term_single_dependency",
                f"fourths1-const{const}",
                {
                    "firsts": [1],
                    "seconds": [1],
                    "thirds": [1],
                    "fourths": some_numbers,
                    "fifths": [1],
                    "constants": [const],
                },
            )
            for const in some_numbers
        ],
        *[
            (
                "long_term_single_dependency",
                f"fifths1-const{const}",
                {
                    "firsts": [1],
                    "seconds": [1],
                    "thirds": [1],
                    "fourths": [1],
                    "fifths": some_numbers,
                    "constants": [const],
                },
            )
            for const in some_numbers
        ],
        # Same issue, go only through lists of 10
        *[
            (
                "long_term_single_dependency",
                f"generic-const{const}",
                {
                    "firsts": list(range(1, 11)),
                    "seconds": list(range(1, 11)),
                    "thirds": list(range(1, 11)),
                    "fourths": list(range(1, 11)),
                    "fifths": list(range(1, 11)),
                    "constants": [const],
                },
            )
            for const in some_numbers
        ],
        # Short term configurations
        *[
            (
                "short_term_single_dependency",
                f"const-{const}",
                {"firsts": some_numbers, "constants": [const]},
            )
            for const in some_numbers
        ],
    ]
    """
    All configurations used to generate the datasets.
    This list generates a total of 1420 datasets.
    Most of them are very similar, and do not need to be used in analysis.
    """

    generator = SequenceGenerator(wanted_length=100)
    for (key, case_name, args) in configurations_to_use:
        generated_log = generator.generate_log(key, **args)
        success = dumps(join(LOGPATH, f"{key}-{case_name}"), generated_log)
        if not success:
            raise OSError("Failed to dump data to disk..")
        else:
            print(f"Success: '{key}-{case_name}'")


def generate_datasets() -> None:
    """
    Generates all datasets.
    """

    # Datasets from XES
    print("Generating datasets from XES...")
    transform()
    print("Done!")

    # Datasets from generators
    print("Generating datasets with generators...")
    generate()
    print("Done!")


if __name__ == "__main__":
    generate_datasets()

else:
    print(
        "File (generate_datasets.py) imported. If this isn't to generate documentation,\
         what are you doing?"
    )
