from Token.DigitToken import DigitToken
from Token.OperatorToken import OperatorToken
from Token.StringToken import StringToken
from Token.Token import Token
from Token.VariableToken import VariableToken


class ExpressionParser(object):
    @staticmethod
    def get_first_from_string(p_expression):
        """
        Получение первой лексемы из строки
        Текст лексемы изсключается из исходной строки
        :param p_expression: Строка
        :return: Лексема, обновленная строка
        """
        expression = p_expression.lstrip()
        token = Token()
        if len(expression) == 0:
            pass
        elif ExpressionParser.is_delimiter(expression[0]):
            token = OperatorToken(expression[0:1])
        elif ExpressionParser.is_quote(expression[0]):
            expression = expression[1:]
            token = StringToken(ExpressionParser.copy_symbols_before_stop_symbol(expression, ExpressionParser.is_quote))
            expression = expression[1:]
        elif expression[0].isalpha():
            token = VariableToken(
                ExpressionParser.copy_symbols_before_stop_symbol(expression, ExpressionParser.is_delimiter))
        elif expression[0].isdigit():
            token = DigitToken(
                ExpressionParser.copy_symbols_before_stop_symbol(expression, ExpressionParser.is_delimiter))
        expression = expression[len(token.text):]
        return token, expression

    @staticmethod
    def is_delimiter(p_character):
        """
        Предикат "Является символов разделителем"
        :param p_character: Символ
        """
        if " +-/*%^=()".find(p_character) > -1:
            return True
        else:
            return False

    @staticmethod
    def is_quote(p_character):
        """
        Предикат "Является символом кавычки"
        :param p_character: Символ
        """
        if "\"".find(p_character) > -1:
            return True
        else:
            return False

    @staticmethod
    def copy_symbols_before_stop_symbol(p_expression, p_predicate):
        """
        Копирование символов до символа разделителя
        :param p_expression: Строка
        :param p_predicate: Предикат, определяющий символ разделитель
        :return: Результирующая строка
        """
        result = ""
        for character in p_expression:
            if p_predicate(character):
                break
            result += character
        return result
