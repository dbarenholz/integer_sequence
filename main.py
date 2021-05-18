# ! /home/dan/miniconda3/bin/conda "run -n internship python"
# -*- coding: utf-8 -*-
from typing import Any
from os import listdir
from os.path import join, isfile

# Own
from generator import XESTransformator

from helper import DATAPATH

if __name__ == "__main__":
    # === anything below this line is testing code === #
    transformer = XESTransformator()

    test_log = "./test/sample_log.xes"

    DATASETS = [
        join(DATAPATH, file)
        for file in listdir(DATAPATH)
        if isfile(join(DATAPATH, file))
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
