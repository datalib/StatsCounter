from __future__ import division
from pytest import raises
from statscounter import StatsCounter, stats
from statscounter.statscounter import MultipleMostCommonValuesError

class TestStatsCounter:
	counter_ints = StatsCounter([1,1,2,3,4])
	counter_ints_with_two_modes = StatsCounter([1,1,2,3,4,4])
	counter_chars = StatsCounter('aabccd')
	
	def test_key_types_distribution(self):
		ci = self.counter_ints.key_types_distribution()
		ci2 = self.counter_ints_with_two_modes.key_types_distribution()
		cc = self.counter_chars.key_types_distribution()
		
		assert ci == StatsCounter(['int'])
		assert ci2 == StatsCounter(['int'])
		assert cc == StatsCounter(['str']) 
		
	def test_mean(self):
		m = self.counter_ints_with_two_modes.mean()
		d = 15/6
		assert m == d
	
	def test_mean_throws_exception(self):
		with raises(TypeError):
			self.counter_chars.mean()
	
	def test_median(self):
		m = self.counter_ints_with_two_modes.median()
		assert m == 2.5
		
	def test_median_throws_exception(self):
		with raises(TypeError):
			self.counter_chars.median()
		
	def test_median_low(self):
		m = self.counter_ints_with_two_modes.median_low()
		assert m == 2		
	
	def test_median_low_throws_exception(self):
		with raises(TypeError):
			self.counter_chars.median_low()
	
	def test_median_high(self, ):
		m = self.counter_ints_with_two_modes.median_high()
		assert m == 3
		
	def test_median_high_throws_exception(self):
		with raises(TypeError):
			self.counter_chars.median_high()

	def test_median_grouped(self, ):
		m = self.counter_ints_with_two_modes.median_grouped()
		assert m == 2.5
		
	def test_median_grouped_throws_exception(self):
		with raises(TypeError):
			self.counter_chars.median_grouped()	
	
	def test_mode(self, ):
		m = self.counter_ints.mode()
		assert m == 1
		
	def test_mode_throws_exception(self):
		with raises(stats.StatisticsError):
			self.counter_ints_with_two_modes.mode()

	def test_variance(self):
		m = self.counter_ints_with_two_modes.variance()
		assert m == 1.9

	def test_stdev(self, ):
		m = self.counter_ints_with_two_modes.stdev()
		assert m == 1.378404875209022

	def test_pvariance(self):
		m = self.counter_ints_with_two_modes.pvariance()
		assert m == 1.5833333333333333

	def test_pstdev(self, ):
		m = self.counter_ints_with_two_modes.pstdev()
		assert m == 1.2583057392117916
	
	def test_argmax(self):
		m = self.counter_ints.argmax()
		assert m == 1
		
	def test_argmax_throws_exception(self):
		with raises(MultipleMostCommonValuesError):
			m = self.counter_ints_with_two_modes.argmax()

	def test_max(self):
		m = self.counter_ints.max()
		assert m == 2

	def test_max_throws_exception(self):
		with raises(MultipleMostCommonValuesError):
			m = self.counter_ints_with_two_modes.max()
		
	def test_normalize(self):
		pdist = StatsCounter({1: 1, 2: 2, 3: 1}).normalize()
		assert pdist == {
			1: 0.25,
			2: 0.50,
			3: 0.25,
		}
		
	def test_get_weighted_random_value(self):
		wrv = StatsCounter(a=10, b=3).get_weighted_random_value()
		assert wrv == "a" or "b"
		
	def test_transform(self):
		dist = StatsCounter({
		    'of': 0.20, 
		    'the': 0.50, 
		    'that': 0.10, 
		    'from': 0.20
		})
		
		dist = dist.transform(lambda word, prob: word.startswith('t'))
		
		assert dist == StatsCounter({True: 0.6, False: 0.4})