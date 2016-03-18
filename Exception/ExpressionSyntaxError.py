from Exception.LexicalParserException import LexicalParserException


class ExpressionSyntaxError(LexicalParserException):
    """
    Исключение "Синтаксическая ошибка"
    """

    def __init__(self):
        """
        Конструктор
        """
        LexicalParserException.__init__(self, "Синтаксическая ошибка")
