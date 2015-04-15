from __future__ import absolute_import, division
"""StatsCounter

This module is derived from the stats module available in Python 3.4

https://hg.python.org/cpython/file/3.4/Lib/statistics.py

Many a times I found myself wanting to to run simple averaging, summation,
variance-calculating methods on the wonderful built-in collections.Counter
class, and I would always include a those "helper" functions that allowed
me to do just that.

After the n-th time of doing the above mentioned ritual, I decided to look
at the statistics module in Python3, and I was surprised to see that most
of the code was written in Python that can be easily back-ported.
"""

from collections import Counter

import math

from statscounter.stats import *

class StatisticsError(ValueError):
    pass


class StatsCounter(Counter):
    def __init__(self,*args, **kwds):
        super(StatsCounter, self).__init__(*args, **kwds)


    def mean(self):
        """Return the sample arithmetic mean of data.

        >>> mean([1, 2, 3, 4, 4])
        2.8

        >>> from fractions import Fraction as F
        >>> mean([F(3, 7), F(1, 21), F(5, 3), F(1, 3)])
        Fraction(13, 21)

        >>> from decimal import Decimal as D
        >>> mean([D("0.5"), D("0.75"), D("0.625"), D("0.375")])
        Decimal('0.5625')

        If ``data`` is empty, StatisticsError will be raised.
        """
        data = self.values()
        if iter(data) is data:
            data = list(data)
        n = len(data)
        if n < 1:
            raise StatisticsError('mean requires at least one data point')
        return _sum(data)/n
