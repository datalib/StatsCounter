from __future__ import absolute_import
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
import statscounter.stats as stats


class WrongVariableTypeError(ValueError):
	"""You cannot find the 'expected value' (mean) of a distribution
	of categorical (nominal) random variables (for example, a 
	distribution of words is equivalent to a categorical variable).
	It makes no sense to find the average word.
	"""
	pass


class StatsCounter(Counter):
	def mean(self):
		""" AKA Expectation
		"""
		try:
			return stats.mean(self.elements())
		except (TypeError):
			raise WrongVariableTypeError("Distribution is not a numerical type.")
		
	def expectation(self):
		"""
		"""
		return self.mean()

	def median(self, ):
		"""
		"""
		return stats.median(self.elements())

	def median_low(self):
		"""
		"""
		return stats.median_low(self.elements())

	def median_high(self):
		"""
		"""
		return stats.median_high(self.elements())

	def median_grouped(self):
		"""
		"""
		return stats.median_grouped(self.elements())

	def mode(self):
		"""
		"""
		return stats.mode(self.elements())

	def variance(self):
		"""
		"""
		return stats.variance(self.elements())

	def pvariance(self):
		"""
		"""
		return stats.pvariance(self.elements())

	def stdev(self, ):
		"""
		"""
		return stats.stdev(self.elements())

	def pstdev(self):
		"""
		"""
		return stats.pstdev(self.elements())

	def best_pair(self):
		return self.most_common(1)[0]

	def argmax(self):
		"""
		"""
		key, _ = self.best_pair()
		return key

	def max(self):
		"""
		"""
		_, value = self.best_pair()
		return value

	def normalize(self):
		"""
		Sum the values in a Counter, then create a new Counter 
		where each new value (while keeping the original key) 
		is equal to the original value divided by sum of all the
		original values (this is sometimes referred to as the 
		normalization constant). 
		https://en.wikipedia.org/wiki/Normalization_(statistics)
		"""
		total = sum(self.values())
		stats = {k: (v / float(total)) for k, v in self.items()}
		return StatsCounter(stats)
	
	def get_weighted_random_value(self):
		"""
		This will generate a value by creating a cumulative distribution, 
		and a random number, and selecting the value who's cumulative 
		distribution interval contains the generated random number. 
		
		For example, if there's 0.7 chance of generating the letter "a"
		and 0.3 chance of generating the letter "b", then if you were to 
		pick one letter 100 times over, the number of a's and b's you 
		would have are likely to be around 70 and 30 respectively.
		
		The mechanics are known as "Cumulative distribution functions"
		(https://en.wikipedia.org/wiki/Cumulative_distribution_function)
		"""
		from bisect import bisect
		from random import random
		#http://stackoverflow.com/questions/4437250/choose-list-variable-given-probability-of-each-variable
		
		total = sum(self.values())
		
		P = [(k, (v / float(total))) for k, v in self.items()]
		
		cdf = [P[0][1]]
		for i in range(1, len(P)):
			cdf.append(cdf[-1] + P[i][1])
			
		return P[bisect(cdf, random())][0]
		
		
	def transform(self, key):
		"""
		"""
		dist = self
		newdist = StatsCounter()
		
		for k, v in dist.items():
			newdist[key(k, v)] += v
		
		return newdist