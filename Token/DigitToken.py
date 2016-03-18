from Token.Token import Token
from Value.DigitValue import DigitValue


class DigitToken(Token):
    """
    Лексема "Число"
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
        :return: Представление в виде значения
        """
        return DigitValue(self.text)
