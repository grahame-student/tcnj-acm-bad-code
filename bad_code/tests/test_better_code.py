from unittest import TestCase
import re

from bad_code.bad import BetterCode
from hamcrest import assert_that, equal_to, is_not


class TestBetterCode(TestCase):
    def test_get_random_alphabet_returns_26_chars(self):
        better = BetterCode()
        result = better.get_random_alphabet()
        assert_that(len(result), equal_to(26))

    def test_get_random_alphabet_returns_lower_case_string(self):
        better = BetterCode()
        result = better.get_random_alphabet()
        assert_that(result, equal_to(result.lower()))

    def test_get_random_alphabet_returns_string_with_26_unique_chars(self):
        better = BetterCode()
        result = better.get_random_alphabet()
        assert_that(len(''.join(set(result)), equal_to(26)))

    def test_get_random_alphabet_returns_string_with_26_unique_chars(self):
        better = BetterCode()
        string = better.get_random_alphabet()
        pattern = re.compile("[a-z]+")
        assert_that(pattern.fullmatch(string), is_not(equal_to(None)))
