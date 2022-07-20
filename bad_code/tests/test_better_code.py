import re
from unittest import TestCase

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
        assert_that(len("".join(set(result))), equal_to(26))

    def test_get_random_alphabet_returns_string_with_only_chars_from_a_to_z(self):
        better = BetterCode()
        string = better.get_random_alphabet()
        pattern = re.compile("[a-z]+")
        assert_that(pattern.fullmatch(string), is_not(equal_to(None)))

    def test_howdy_returns_1_when_passed_m(self):
        better = BetterCode()
        assert_that(better.howdy("m"), equal_to(1))

    def test_howdy_returns_10_when_passed_10234(self):
        better = BetterCode()
        assert_that(better.howdy("10234"), equal_to(10))

    def test_howdy_returns_1_when_passed_sick_dudesfsd(self):
        better = BetterCode()
        assert_that(better.howdy("sick dudesfsd"), equal_to(1))

    def test_howdy_returns_19_when_passed_a(self):
        better = BetterCode()
        assert_that(better.howdy("a"), equal_to(19))
