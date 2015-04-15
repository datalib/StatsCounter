from __future__ import absolute_import, division
"""StatsCounter

This module is derived from the stats module available
in Python 3.4:

https://hg.python.org/cpython/file/3.4/Lib/statistics.py

Many a times I found myself wanting to to run simple
averaging, summation, variance-calculating methods on the
wonderful built-in collections.Counter class, and I would
always include a those "helper" functions that allowed
me to do just that.

After the n-th time of doing the above mentioned ritual,
I decided to look at the statistics module in Python3,
and I was surprised to see that most of the code was
written in Python that can be easily back-ported.

Cheers,
Rodrigo
"""

from collections import Counter

from statscounter import stats


class StatsCounter(Counter):
    def __init__(self,*args, **kwds):
        super(StatsCounter, self).__init__(*args, **kwds)


    def mean(self):
        """
        """
        return stats.mean(self.values())

    def median(self, ):
        """
        """
        return stats.median(self.values())

    def median_low(self):
        """
        """
        return stats.median_low(self.values())

    def median_high(self):
        """
        """
        return stats.median_high(self.values())

    def median_grouped(self):
        """
        """
        return stats.median_grouped(self.values())

    def mode(self):
        """
        """
        return stats.mode(self.values())

    def variance(self):
        """
        """
        return stats.variance(self.values())

    def pvariance(self):
        """
        """
        return stats.pvariance(self.values())

    def stdev(self, ):
        """
        """
        return stats.stdev(self.values())

    def pstdev(self):
        """
        """
        return stats.pstdev(self.values())

    def argmax(self):
        """
        """
        return self.most_common(1)[0][0]

    def max(self):
        """
        """
        return self.most_common(1)[0][1]
