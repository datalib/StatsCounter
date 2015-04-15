from __future__ import division
from unittest import TestCase

from statscounter.stats import _sum, mean, median, median_low, \
            median_high, median_grouped, mode, \
            stdev, pstdev, variance, pvariance


class TestStats(TestCase):
    def setUp(self):
        self.ints = [1, 2, 3, 4, 4, 6]
        self.floats = [3, 2.25, 4.5, -0.5, 1.0, 0.75]

    def test_sum(self):
        i = _sum(self.ints)
        assert i == 20
        assert _sum(self.ints, 2) == i + 2

        f = _sum(self.floats)
        assert f == 11.0
        assert _sum(self.floats, 0.75) == f + 0.75

    def test_mean(self):
        m = mean(self.ints)
        d = (1+2+3+4+4+6)/6
        assert m == d

    def test_median(self):
        m = median(self.ints)
        assert m == 3.5

    def test_median_low(self):
        m = median_low(self.ints)
        assert m == 3

    def test_median_high(self, ):
        m = median_high(self.ints)
        assert m == 4

    def test_median_grouped(self, ):
        m = median_grouped(self.ints)
        assert m == 3.5

    def test_variance(self):
        m = variance(self.ints)
        assert m == 3.066666666666667

    def test_stdev(self, ):
        m = stdev(self.ints)
        assert m == 1.7511900715418263
