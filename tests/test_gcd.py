from unittest import TestCase
from functions.gcd import gcd

class GcdFunctionTestCase(TestCase):
    def test_10_gcd_5_returns_5(self):
        self.assertEqual(5, gcd(10, 5))

    def test_99_gcd_45_returns_9(self):
        self.assertEqual(9, gcd(99, 45))

    def test_33_gcd_27_returns_3(self):
        self.assertEqual(3, gcd(33, 27))

    def test_3_gcd_45_returns_3(self):
        self.assertEqual(3, gcd(3, 45))

    def test_10_gcd_100_returns_10(self):
        self.assertEqual(10, gcd(10, 100))

