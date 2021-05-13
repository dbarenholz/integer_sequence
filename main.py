# ! /home/dan/miniconda3/bin/conda "run -n internship python"
# -*- coding: utf-8 -*-
from typing import Any
from os import getcwd, listdir
from os.path import join, isfile

# Own
from generator import XESTransformator

if __name__ == "__main__":
    # === anything below this line is testing code === #
    transformer = XESTransformator()

    test_log = "./data/small_log.xes"

    path_to_datasets = join(getcwd(), "data")
    DATASETS = [
        join(path_to_datasets, file)
        for file in listdir(path_to_datasets)
        if isfile(join(path_to_datasets, file))
    ]

    transformed = transformer.transform(test_log)

    def show(log: Any) -> None:
        for i, l in enumerate(log):
            print(f"Trace {i}: {l}")

    show(transformed)


else:
    print(
        "File imported. If this isn't to generate documentation,\
         what are you doing?"
    )
