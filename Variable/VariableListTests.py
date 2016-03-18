from unittest import TestCase

from Value.DigitValue import DigitValue
from Variable.VariableList import VariableList


class VariableListTests(TestCase):
    def test_AddVariableToList(self):
        variables = VariableList()
        variables["c"].value = DigitValue(10)
        self.assertEqual("c", variables["c"].name)
        self.assertEqual(10, variables["c"].value.to_double())
