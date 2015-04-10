from unittest import TestCase

from statscounter import util


class TestUtil(TestCase):
    def test_sum(self):
        s = util._sum([3, 2.25, 4.5, -0.5, 1.0], 0.75)
        assert s == 11.0
