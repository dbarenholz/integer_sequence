from generator.XESTransformator import XESTransformator
from generator.SequenceGenerator import SequenceGenerator
from inspect import getmembers

__all__ = ["SequenceGenerator", "XESTransformator"]

# Override pdoc to also document private methods, but not __class__ methods.
__pdoc__ = {}
for cls in (XESTransformator, SequenceGenerator):
    for name, value in getmembers(cls):
        if name.startswith("_") and not name.endswith("_"):
            __pdoc__[cls.__name__ + "." + name] = True
