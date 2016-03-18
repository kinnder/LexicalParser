from Exception.LexicalParserException import LexicalParserException


class DivisionByZero(LexicalParserException):
    """
    Исключение "Деление на ноль"
    """

    def __init__(self):
        """
        Конструктор
        """
        LexicalParserException.__init__(self, "Деление на ноль")
