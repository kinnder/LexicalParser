from unittest import TestCase
from Value.DigitValue import DigitValue
from Exception.DivisionByZero import DivisionByZero


class DigitValueTests(TestCase):
    def test_ToDouble_Double(self):
        value = DigitValue(-11.3)
        self.assertEqual(-11.3, value.to_double())

    def test_ToDouble_SyntaxErrorException(self):
        value = DigitValue("abc")
        with self.assertRaises(SyntaxError):
            value.to_double()

    def test_Subtraction(self):
        value1 = DigitValue(20)
        value2 = DigitValue(10)
        self.assertEqual("10.0", value1.subtract(value2).__str__())

    def test_Addition(self):
        value1 = DigitValue(20)
        value2 = DigitValue(5)
        self.assertEqual("25.0", value1.add(value2).__str__())

    def test_Multiplication(self):
        value1 = DigitValue(3)
        value2 = DigitValue(5)
        self.assertEqual("15.0", value1.multiply(value2).__str__())

    def test_Division(self):
        value1 = DigitValue(30)
        value2 = DigitValue(5)
        self.assertEqual("6.0", value1.divide(value2).__str__())

    def test_Division_DivisionByZeroException(self):
        value1 = DigitValue(10)
        value2 = DigitValue(0)
        with self.assertRaises(DivisionByZero):
            value1.divide(value2)

    def test_Modulo(self):
        value1 = DigitValue(8)
        value2 = DigitValue(5)
        self.assertEqual("3.0", value1.modulo(value2).__str__())

    def test_Modulo_DivisionByZeroException(self):
        value1 = DigitValue(10)
        value2 = DigitValue(0)
        with self.assertRaises(DivisionByZero):
            value1.modulo(value2)

    def test_Power(self):
        value1 = DigitValue(3)
        value2 = DigitValue(2)
        self.assertEqual("9.0", value1.power(value2).__str__())

    def test_Power_Exponential_0(self):
        value1 = DigitValue(23)
        value2 = DigitValue(0)
        self.assertEqual("1.0", value1.power(value2).__str__())

    def test_MinusSign(self):
        value = DigitValue(10)
        self.assertEqual("-10.0", value.minus_sign().__str__())
