from unittest import TestCase

from bad_code.bad import BetterCode
from hamcrest import assert_that, equal_to


class TestBetterCode(TestCase):
    def test_get_random_alphabet_returns_26_chars(self):
        better = BetterCode()
        result = better.get_random_alphabet()
        assert_that(len(result), equal_to(26))
