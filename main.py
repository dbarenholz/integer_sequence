# ! /home/dan/miniconda3/bin/conda "run -n internship python"
# -*- coding: utf-8 -*-
from generator.SequenceGenerator import SequenceGenerator

if __name__ == "__main__":
    # Create a generator object
    generator = SequenceGenerator(wanted_length=20)

    fib_log = generator.generate_log(
        "fib", firsts=[1, 2, 3, 4, 5], seconds=[1, 2, 3, 4, 5]
    )
    print("=== generated fiblog ===")
    for i, l in enumerate(fib_log):
        print(f"Trace {i}: {l}")

    pascal_log = generator.generate_log(
        "pascal", base_numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    )
    print("=== generated pascallog ===")
    for i, l in enumerate(pascal_log):
        print(f"Trace {i}: {l}")
else:
    print(
        "File imported. If this isn't to generate documentation,\
         what are you doing?"
    )
