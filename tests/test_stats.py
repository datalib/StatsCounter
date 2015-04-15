from __future__ import division
from unittest import TestCase

from statscounter.stats import _sum, mean, median, median_low, \
            median_high, median_grouped, mode, \
            stdev, pstdev, variance, pvariance


def frange(x, y, jump):
    while x < y:
        yield x
        x += jump

class TestStats(TestCase):
    def setUp(self):
        self.ints = list(range(10000))

        self.floats = frange(0, 1, 0.001)

    def test_sum(self):
        i = _sum(self.ints)
        assert i == 49995000

        f = _sum(self.floats)
        assert f == 499.50000000000034

    def test_mean(self):
        m = mean(self.ints)
        d = (49995000)/10000
        assert m == d

    def test_median(self):
        m = median(self.ints)
        assert m == 4999.5

    def test_mode(self):
        m = mode(self.ints + [1])
        assert m == 1

    def test_median_low(self):
        m = median_low(self.ints)
        assert m == 4999

    def test_median_high(self, ):
        m = median_high(self.ints)
        assert m == 5000

    def test_median_grouped(self, ):
        m = median_grouped(self.ints)
        assert m == 4999.5

    def test_variance(self):
        m = variance(self.ints)
        assert m == 8334166.666666667

    def test_stdev(self):
        m = stdev(self.ints)
        assert m == 2886.8956799071675

    def test_pvariance(self):
        m = pvariance(self.ints)
        assert m == 8333333.25

    def test_pstdev(self):
        m = pstdev(self.ints)
        assert m == 2886.751331514372
