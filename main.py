# ! /home/dan/miniconda3/bin/conda "run -n internship python"
# -*- coding: utf-8 -*-
from typing import Any

# Own
from generator import SequenceGenerator

if __name__ == "__main__":
    # Create a generator object
    generator = SequenceGenerator(wanted_length=100)

    # === anything below this line is testing code === #
    def show(log: Any) -> None:
        for i, l in enumerate(log):
            print(f"Trace {i}: {l}")


else:
    print(
        "File imported. If this isn't to generate documentation,\
         what are you doing?"
    )
