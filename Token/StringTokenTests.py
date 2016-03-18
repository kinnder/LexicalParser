from unittest import TestCase

from Token.StringToken import StringToken
from Value.StringValue import StringValue


class StringTokenTests(TestCase):
    def test_PutAsFirstInString(self):
        token = StringToken("abc")
        self.assertEqual("\"abc\" \"def\"", token.put_as_first_in_string("\"def\""))

    def test_ToValue(self):
        token = StringToken("abc")
        self.assertIsInstance(token.to_value(), StringValue)
