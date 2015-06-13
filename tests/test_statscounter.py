from __future__ import division
from pytest import raises
from statscounter import StatsCounter, stats


class TestStatsCounter:
    counter_ints = StatsCounter({str(s):s for s in range(1000)})

    def test_mean_int(self):
        m = self.counter_ints.mean()
        d = 499500/1000
        assert m == d

    def test_median_low(self):
        m = self.counter_ints.median_low()
        assert m == 499

    def test_median_high(self, ):
        m = self.counter_ints.median_high()
        assert m == 500

    def test_median_grouped(self, ):
        m = self.counter_ints.median_grouped()
        assert m == 499.5

    def test_mode(self):
        with raises(stats.StatisticsError):
            self.counter_ints.mode()

    def test_variance(self):
        m = self.counter_ints.variance()
        assert m == 83416.66666666667

    def test_stdev(self, ):
        m = self.counter_ints.stdev()
        assert m == 288.8194360957494

    def test_pvariance(self):
        m = self.counter_ints.pvariance()
        assert m == 83333.25

    def test_pstdev(self, ):
        m = self.counter_ints.pstdev()
        assert m == 288.6749902572095

    def test_argmax(self):
        m = self.counter_ints.argmax()
        assert m == '999'

    def test_max(self):
        m = self.counter_ints.max()
        assert m == 999

    def test_pdist(self):
        pdist = StatsCounter({1: 1, 2: 2, 3: 1}).pdist()
        assert pdist == {
            1: 0.25,
            2: 0.50,
            3: 0.25,
        }
