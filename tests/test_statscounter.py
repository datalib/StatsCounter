from __future__ import division

from unittest import TestCase

from statscounter import StatsCounter

class TestStatsCounter(TestCase):
    def setUp(self):
        self.counter_ints = StatsCounter(a=1, b=2, c=3, d=4, e=4, f=6)
        #self.counter_floats =

    def test_mean_int(self):
        m = self.counter_ints.mean()
        d = (1+2+3+4+4+6)/6
        assert m == d

    def test_median_low(self):
        m = self.counter_ints.median_low()
        assert m == 3

    def test_median_high(self, ):
        m = self.counter_ints.median_high()
        assert m == 4

    def test_median_grouped(self, ):
        m = self.counter_ints.median_grouped()
        assert m == 3.5

    def test_variance(self):
        m = self.counter_ints.variance()
        assert m == 3.066666666666667

    def test_stdev(self, ):
        m = self.counter_ints.stdev()
        assert m == 1.7511900715418263
