## TODO: Fix shebang line for conda
#! /home/dan/miniconda3/bin/conda "run -n internship python"
# -*- coding: utf-8 -*-
import sys

from generator.SequenceGenerator import SequenceGenerator

if __name__ == "__main__":
    # Create a generator object
    generator = SequenceGenerator(wanted_length = 20)

    # print(tuple(generate_trace("fib", first=1, second=1)))
    # print(tuple(generate_trace("pascal", base_number=1)))
    fib_log = generator.generate_log(
        "fib",
        firsts = [1, 2, 3, 4, 5],
        seconds = [1, 2, 3, 4, 5]
    )
    print("=== generated fiblog ===")
    for i, l in enumerate(fib_log):
        print(f"Trace {i}: {l}")
    
    pascal_log = generator.generate_log(
        "pascal",
        base_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    )
    print("=== generated pascallog ===")
    for i, l in enumerate(pascal_log):
        print(f"Trace {i}: {l}")
else:
    print("Do not import this file. Thank you.")
    sys.exit("File was imported. Don't.")