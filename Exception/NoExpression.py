from Exception.LexicalParserException import LexicalParserException


class NoExpression(LexicalParserException):
    """
    Исключение "Выражение отсутствует"
    """

    def __init__(self):
        """
        Конструктор
        """
        LexicalParserException.__init__(self, "Выражение отсутствует")
