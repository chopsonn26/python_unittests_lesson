from unittest import TestCase
from functions.email import is_correct_email

class EmailFunctionTestCase(TestCase):
    def test_email_esena_returns_True(self):
        self.assertEqual(True, is_correct_email("esena@gmail.com")

    def test_email_theesena_returns_True(self):
        self.assertEqual(True, is_correct_email("theesena@mail.com")

    def test_email_esena_returns_False(self):
        self.assertEqual(False, is_correct_email("esena.12@@gmail.com")

    def test_email_gmail_False(self):
        self.assertEqual(False, is_correct_email("@gmail.com")

    def test_email_12gmail_False(self):
        self.assertEqual(False, is_correct_email("esena.12gmail.com")

