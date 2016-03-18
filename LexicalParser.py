from Exception.ExpressionSyntaxError import ExpressionSyntaxError
from Exception.NoExpression import NoExpression
from Exception.UnBalancedBrackets import UnBalancedBrackets
from Token.DigitToken import DigitToken
from Token.ExpressionParser import ExpressionParser
from Token.StringToken import StringToken
from Token.Token import Token
from Token.VariableToken import VariableToken
from Value.Value import Value
from Variable.VariableList import VariableList


class LexicalParser(object):
    """
    Синтаксический анализатор
    """

    def __init__(self):
        """
        Конструктор
        """
        self.expression = ""
        self.variables = VariableList()
        self.token = Token()
        self.savedToken = Token()

    def evaluate(self, p_expression):
        """
        Входная точка анализатора
        :param p_expression: Выражение
        :return: Результат вычислений
        """
        result = Value()
        self.expression = p_expression
        self.get_token_from_string()
        if self.token.is_empty():
            raise NoExpression()
        result = self.evaluate_operators_of_rank1(result)
        if not self.token.is_empty():
            raise ExpressionSyntaxError()
        return result

    def evaluate_operators_of_rank1(self, p_result):
        """
        Вычисление операторов 1го ранга
        :param p_result: Результат вычислений
        :return: Результат вычислений
        """
        if type(self.token) is VariableToken:
            self.save_token()
            self.get_token_from_string()
            if not self.token.is_assign():
                self.restore_token()
            else:
                self.get_token_from_string()
                result = self.evaluate_operators_of_rank2(p_result)
                self.variables[self.savedToken.text].value = result
                return result
        return self.evaluate_operators_of_rank2(p_result)

    def evaluate_operators_of_rank2(self, p_result):
        """
        Вычисление операторов 2го ранга
        :param p_result: Результат вычисления
        :return: Результат вычисления
        """
        result = self.evaluate_operators_of_rank3(p_result)
        while self.token.is_plus() or self.token.is_minus():
            operation = self.token.text
            self.get_token_from_string()
            partial_result = self.evaluate_operators_of_rank3(Value())
            if operation == "-":
                result = result.subtract(partial_result)
            elif operation == "+":
                result = result.add(partial_result)
        return result

    def evaluate_operators_of_rank3(self, p_result):
        """
        Вычисление операторов 3го ранга
        :param p_result: Результат вычисления
        :return: Результат вычисления
        """
        result = self.evaluate_operators_of_rank4(p_result)
        while self.token.is_multiplication() or self.token.is_division() or self.token.is_modulo():
            operation = self.token.text
            self.get_token_from_string()
            partial_result = self.evaluate_operators_of_rank4(Value())
            if operation == "*":
                result = result.multiply(partial_result)
            elif operation == "/":
                result = result.divide(partial_result)
            elif operation == "%":
                result = result.modulo(partial_result)
        return result

    def evaluate_operators_of_rank4(self, p_result):
        """
        Вычисление операторов 4го ранга
        :param p_result: Результат вычисления
        :return: Результат вычисления
        """
        result = self.evaluate_operators_of_rank5(p_result)
        while self.token.is_power():
            partial_result = Value()
            self.get_token_from_string()
            partial_result = self.evaluate_operators_of_rank4(partial_result)
            result = result.power(partial_result)
        return result

    def evaluate_operators_of_rank5(self, p_result):
        """
        Вычисление операторов 5го ранга
        :param p_result: Результат вычисления
        :return: Результат вычисления
        """
        operation = ""
        if self.token.is_plus() or self.token.is_minus():
            operation = self.token.text
            self.get_token_from_string()
        result = self.evaluate_operators_of_rank6(p_result)
        if operation == "-":
            result = result.minus_sign()
        return result

    def evaluate_operators_of_rank6(self, p_result):
        """
        Вычисление операторов 6го ранга
        :param p_result: Результат вычисления
        :return: Результат вычисления
        """
        if self.token.is_opening_bracket():
            self.get_token_from_string()
            result = self.evaluate_operators_of_rank2(p_result)
            if not self.token.is_closing_bracket():
                raise UnBalancedBrackets()
            self.get_token_from_string()
        else:
            result = self.evaluate_operators_of_rank7()
        return result

    def evaluate_operators_of_rank7(self):
        """
        Вычисление операторов 7го ранга
        :return: Результат вычисления
        """
        if type(self.token) is DigitToken or type(self.token) is StringToken:
            result = self.token.to_value()
        elif type(self.token) is VariableToken:
            result = self.variables[self.token.text].value
        else:
            raise ExpressionSyntaxError()
        self.get_token_from_string()
        return result

    def return_token_to_string(self):
        """
        Возвращение лексемы в выражение
        """
        self.expression = self.token.put_as_first_in_string(self.expression)

    def get_token_from_string(self):
        """
        Получение лексемы из выражения
        """
        self.token, self.expression = ExpressionParser.get_first_from_string(self.expression)

    def save_token(self):
        """
        Сохранение лексемы в буфере
        """
        self.savedToken = Token.copy(self.token)

    def restore_token(self):
        """
        Получение лексемы из буфера
        """
        self.return_token_to_string()
        self.token = Token.copy(self.savedToken)
