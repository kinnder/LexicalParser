from unittest import TestCase

from Exception.ExpressionSyntaxError import ExpressionSyntaxError
from Exception.NoExpression import NoExpression
from Exception.UnBalancedBrackets import UnBalancedBrackets
from LexicalParser import LexicalParser


class LexicalParserTests(TestCase):
    def setUp(self):
        self.parser = LexicalParser()

    def test_Addition(self):
        self.assertEqual("10.0", self.parser.evaluate("5+5").__str__())
        self.assertEqual("string", self.parser.evaluate("\"str\"+\"ing\"").__str__())

    def test_Subtraction(self):
        self.assertEqual("-5.0", self.parser.evaluate("5-10").__str__())

    def test_Multiplication(self):
        self.assertEqual("25.0", self.parser.evaluate("5*5").__str__())

    def test_Division(self):
        self.assertEqual("10.0", self.parser.evaluate("30/3").__str__())

    def test_Modulo(self):
        self.assertEqual("3.0", self.parser.evaluate("8%5").__str__())

    def test_Power(self):
        self.assertEqual("9.0", self.parser.evaluate("3^2").__str__())

    def test_Brackets(self):
        self.assertEqual("30.0", self.parser.evaluate("10*(2+1)").__str__())

    def test_Variable(self):
        self.assertEqual("2.5", self.parser.evaluate("A = 10 / 4").__str__())
        self.assertEqual("2.5", self.parser.evaluate("F = A").__str__())
        self.assertEqual("-46.25", self.parser.evaluate("C = A * (F - 21)").__str__())

    def test_MinusSign(self):
        self.assertEqual("-2.0", self.parser.evaluate("-2").__str__())

    def test_SyntaxErrorException(self):
        with self.assertRaises(ExpressionSyntaxError):
            self.parser.evaluate("10*")

    def test_UnbalancedBracketsException(self):
        with self.assertRaises(UnBalancedBrackets):
            self.parser.evaluate("(10+5")

    def test_NoExpressionException(self):
        with self.assertRaises(NoExpression):
            self.parser.evaluate("")
