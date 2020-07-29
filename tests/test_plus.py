from unittest import TestCase
from functions.plus import plus

class PlusFunctionTestCase(TestCase):
    def test_1_plus_1_returns_2(self):

        self.assertEqual(2, plus(1,1))

    def test_1555_plus_445is_2000(self):
        self.assertEqual(2000,plus(1555,445))