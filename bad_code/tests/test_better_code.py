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

    def test_howdy_returns_10_when_passed_4(self):
        better = BetterCode()
        assert_that(better.howdy("4"), equal_to(10))

    def test_the_stuff_returns_set_of_numbers(self):
        better = BetterCode()
        expected_set = {0, -12, -1, -8, -6, -4, -3, -2}
        assert_that(better.the_stuff(), equal_to(expected_set))

    def test_probably_okay_returns_set_of_numbers(self):
        better = BetterCode()
        expected_set = {0, 1}
        assert_that(better.probably_okay(), equal_to(expected_set))

    def test_oh_my_returns_set_of_0_1_20_when_passed_1_2_0(self):
        better = BetterCode()
        expected_set = {0, 1, 20}
        assert_that(better.oh_my(1, 2, 0), equal_to(expected_set))

    def test_oh_my_returns_set_of_16_3_7_when_passed_minus_2_2_minus_2(self):
        better = BetterCode()
        expected_set = {16, 3, 7}
        assert_that(better.oh_my(-2, 2, -2), equal_to(expected_set))

    def test_oh_my_returns_set_of_88_105_180_when_passed_1_2_10(self):
        better = BetterCode()
        expected_set = {88, 105, 180}
        assert_that(better.oh_my(1, 2, 10), equal_to(expected_set))

    def test_oh_my_returns_set_of_0_12_5_when_passed_minus_2_5_minus_2(self):
        better = BetterCode()
        expected_set = {0, 12, 5}
        assert_that(better.oh_my(-2, 5, -2), equal_to(expected_set))
