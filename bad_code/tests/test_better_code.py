from unittest import TestCase

from hamcrest import assert_that, equal_to
from bad import BetterCode


class TestBetterCode(TestCase):
    def test_(self):
        assert_that(True, equal_to(True))
