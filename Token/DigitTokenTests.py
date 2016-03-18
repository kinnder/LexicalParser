from unittest import TestCase
from Token.DigitToken import DigitToken
from Value.DigitValue import DigitValue


class DigitTokenTests(TestCase):
    def test_ToValue(self):
        token = DigitToken("0")
        self.assertIsInstance(token.to_value(), DigitValue)
