from unittest import TestCase

from Value.StringValue import StringValue


class StringValueTests(TestCase):
    def test_Addition(self):
        value1 = StringValue("str")
        value2 = StringValue("ing")
        self.assertEqual("string", value1.add(value2).__str__())
