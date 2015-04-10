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

from statscounter import util

class StatisticsError(ValueError):
    pass


class StatsCounter(Counter):
    def __init__(self,*args, **kwds):
        super(StatsCounter, self).__init__(*args, **kwds)

    def _ss(self):
        """Return sum of square deviations of sequence data.
        """

        xbar = self.mean()
        data = self.values()
        ss = util._sum((x-xbar)**2 for x in data)
        # The following sum should mathematically equal zero, but due to rounding
        # error may not.
        ss -= util._sum((x-xbar) for x in data)**2/len(data)
        assert not ss < 0, 'negative sum of square deviations: %f' % ss
        return ss

    def mean(self):
        """Return the sample arithmetic mean of data.
        """
        data = self.values()

        if iter(data) is data:
            data = list(data)
        n = len(data)
        if n < 1:
            raise StatisticsError('mean requires at least one data point')
        return util._sum(data)/n

    def median_low(self):
        """Return the low median of numeric data.

        When the number of data points is odd, the middle value is returned.
        When it is even, the smaller of the two middle values is returned.
        """
        data = self.values()

        data = sorted(data)

        n = len(data)
        if n == 0:
            raise Exception("no median for empty data")
        if n%2 == 1:
            return data[n//2]
        else:
            return data[n//2 - 1]

    def median_high(self):
        """Return the high median of data.

        When the number of data points is odd, the middle value is returned.
        When it is even, the larger of the two middle values is returned.
        """
        data = self.values()

        data = sorted(data)

        n = len(data)
        if n == 0:
            raise Exception("no median for empty data")
        return data[n//2]

    def median_grouped(self, interval=1):
        u""""Return the 50th percentile (median) of grouped continuous data.
        >>> counter = StatsCounter(a=1, b=2, c=3, d=4, e=4, f=6)
        >>> counter.median_grouped()
        3.5
        """
        data = self.values()

        data = sorted(data)
        n = len(data)
        if n == 0:
            raise StatisticsError(u"no median for empty data")
        elif n == 1:
            return data[0]
        # Find the value at the midpoint. Remember this corresponds to the
        # centre of the class interval.
        x = data[n//2]
        for obj in (x, interval):
            if isinstance(obj, (unicode, str)):
                raise TypeError(u'expected number but got %r' % obj)
        try:
            L = x - interval/2  # The lower limit of the median interval.
        except TypeError:
            # Mixed type. For now we just coerce to float.
            L = float(x) - float(interval)/2
        cf = data.index(x)  # Number of values below the median interval.
        # FIXME The following line could be more efficient for big lists.
        f = data.count(x)  # Number of data points in the median interval.
        return L + interval*(n/2 - cf)/f

    def variance(self):
        """Return the sample variance of data.

        Use this function when your data is a sample from a population. To
        calculate the variance from the entire population, see ``pvariance``.
        """
        data = self.values()

        if iter(data) is data:
            data = list(data)
        n = len(data)
        if n < 2:
            raise Exception('variance requires at least two data points')
        ss = self._ss()
        return ss/(n-1)


    def pvariance(self):
        """Return the population variance of ``data``.
        """
        data = self.values()
        if iter(data) is data:
            data = list(data)
        n = len(data)
        if n < 1:
            raise StatisticsError('pvariance requires at least one data point')
        ss = self._ss()
        return ss/n

    def stdev(self):
        """Return the square root of the sample variance.

        See ``variance`` for arguments and other details.

        >>> stdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75])
        1.0810874155219827

        """

        var = self.variance()
        try:
            return var.sqrt()
        except AttributeError:
            return math.sqrt(var)


    def pstdev(self):
        """Return the square root of the population variance.
        """
        var = self.pvariance()
        try:
            return var.sqrt()
        except AttributeError:
            return math.sqrt(var)
