try:
    from statistics import *
except ImportError:
    from ._stats import *
