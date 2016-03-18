from Token.Token import Token
from Value.StringValue import StringValue


class StringToken(Token):
    """
    Лексема "Строка"
    """

    def __init__(self, p_text):
        """
        Конструктор
        :param p_text: Текст
        """
        Token.__init__(self, p_text)

    def to_value(self):
        """
        Преобразование в значение
        :return:
        """
        return StringValue(self.text)

    def put_as_first_in_string(self, p_expression):
        """
        Возвращение лексемы в строку
        Текст лексемы вставляется в начало строки
        :param p_expression: Строка
        :return: Результирующая строка
        """
        self.text = "\"" + self.text + "\""
        return Token.put_as_first_in_string(self, p_expression)
