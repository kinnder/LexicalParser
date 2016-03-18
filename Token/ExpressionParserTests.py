from unittest import TestCase

from Token.DigitToken import DigitToken
from Token.ExpressionParser import ExpressionParser
from Token.OperatorToken import OperatorToken
from Token.StringToken import StringToken
from Token.Token import Token
from Token.VariableToken import VariableToken


class ExpressionParserTests(TestCase):
    def test_GetFirstFromString_Token(self):
        expression = ""
        token, expression = ExpressionParser.get_first_from_string(expression)
        self.assertIsInstance(token, Token)
        self.assertTrue(token.is_empty())

    def test_GetFirstFromString_VariableToken(self):
        expression = "abc def"
        token, expression = ExpressionParser.get_first_from_string(expression)
        self.assertIsInstance(token, VariableToken)
        self.assertEqual("abc", token.text)

    def test_GetFirstFromString_StringToken(self):
        expression = "\"abc\" \"def\""
        token, expression = ExpressionParser.get_first_from_string(expression)
        self.assertIsInstance(token, StringToken)
        self.assertEqual("abc", token.text)

    def test_GetFirstFromString_DigitToken(self):
        expression = "12 + 2"
        token, expression = ExpressionParser.get_first_from_string(expression)
        self.assertIsInstance(token, DigitToken)
        self.assertEqual("12", token.text)

    def test_GetFirstFromString_OperatorToken_Plus(self):
        expression = "+"
        token, expression = ExpressionParser.get_first_from_string(expression)
        self.assertIsInstance(token, OperatorToken)
        self.assertTrue(token.is_plus())

    def test_GetFirstFromString_OperatorToken_Minus(self):
        expression = "-"
        token, expression = ExpressionParser.get_first_from_string(expression)
        self.assertIsInstance(token, OperatorToken)
        self.assertTrue(token.is_minus())

    def test_GetFirstFromString_OperatorToken_Division(self):
        expression = "/"
        token, expression = ExpressionParser.get_first_from_string(expression)
        self.assertIsInstance(token, OperatorToken)
        self.assertTrue(token.is_division())

    def test_GetFirstFromString_OperatorToken_Multiplication(self):
        expression = "*"
        token, expression = ExpressionParser.get_first_from_string(expression)
        self.assertIsInstance(token, OperatorToken)
        self.assertTrue(token.is_multiplication())

    def test_GetFirstFromString_OperatorToken_Modulo(self):
        expression = "%"
        token, expression = ExpressionParser.get_first_from_string(expression)
        self.assertIsInstance(token, OperatorToken)
        self.assertTrue(token.is_modulo())

    def test_GetFirstFromString_OperatorToken_Power(self):
        expression = "^"
        token, expression = ExpressionParser.get_first_from_string(expression)
        self.assertIsInstance(token, OperatorToken)
        self.assertTrue(token.is_power())

    def test_GetFirstFromString_OperatorToken_Assign(self):
        expression = "="
        token, expression = ExpressionParser.get_first_from_string(expression)
        self.assertIsInstance(token, OperatorToken)
        self.assertTrue(token.is_assign())

    def test_GetFirstFromString_OperatorToken_OpeningBracket(self):
        expression = "("
        token, expression = ExpressionParser.get_first_from_string(expression)
        self.assertIsInstance(token, OperatorToken)
        self.assertTrue(token.is_opening_bracket())

    def test_GetFirstFromString_OperatorToken_ClosingBracket(self):
        expression = ")"
        token, expression = ExpressionParser.get_first_from_string(expression)
        self.assertIsInstance(token, OperatorToken)
        self.assertTrue(token.is_closing_bracket())

    def test_GetSeveralTokens(self):
        expression = "A = 2"
        token, expression = ExpressionParser.get_first_from_string(expression)
        self.assertIsInstance(token, VariableToken)

        token, expression = ExpressionParser.get_first_from_string(expression)
        self.assertIsInstance(token, OperatorToken)

        token, expression = ExpressionParser.get_first_from_string(expression)
        self.assertIsInstance(token, DigitToken)
