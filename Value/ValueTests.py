from unittest import TestCase

from Exception.UnSupportedOperation import UnSupportedOperation
from Value.Value import Value


class ValueTests(TestCase):
    def setUp(self):
        self.value = Value()

    def test_DataToString(self):
        self.assertEqual("abc", Value("abc").__str__())

    def test_Subtract(self):
        with self.assertRaises(UnSupportedOperation):
            self.value.subtract(self.value)

    def test_Addition(self):
        with self.assertRaises(UnSupportedOperation):
            self.value.add(self.value)

    def test_Multiplication(self):
        with self.assertRaises(UnSupportedOperation):
            self.value.multiply(self.value)

    def test_Division(self):
        with self.assertRaises(UnSupportedOperation):
            self.value.divide(self.value)

    def test_Modulo(self):
        with self.assertRaises(UnSupportedOperation):
            self.value.modulo(self.value)

    def test_Power(self):
        with self.assertRaises(UnSupportedOperation):
            self.value.power(self.value)

    def test_MinusSign(self):
        with self.assertRaises(UnSupportedOperation):
            self.value.minus_sign()
