from unittest import TestCase
from functions.hm27 import print_min

class PrintMinFunctionTestCase(TestCase):
    def test_0_0_print_min_4_returns_negative4(self):
        self.assertEqual(-4, print_min(0, 0, 4))

    def test_0_0_print_min_2_returns_negative2(self):
        self.assertEqual(-2, print_min(0, 0, 2))

    def test_8_8_print_min_8_returns_negative56(self):
        self.assertEqual(-56, print_min(8, 8, 8))

    def test_0_0_print_min_1_returns_negative1(self):
        self.assertEqual(-1, print_min(0, 0, 1))

    def test_0_0_print_min_2_returns_negative4(self):
        self.assertEqual(-4, print_min(0, 2, 2))