from unittest import TestCase

from Token.Token import Token
from Value.Value import Value


class TokenTests(TestCase):
    def test_PutAsFirstInString(self):
        token = Token("abc")
        self.assertEqual("abc def", token.put_as_first_in_string("def"))

    def test_ToValue(self):
        token = Token("abc")
        self.assertIsInstance(token.to_value(), Value)
