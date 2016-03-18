from Exception.LexicalParserException import LexicalParserException


class UnSupportedOperation(LexicalParserException):
    """
    Исключение "Неподдерживаемая операция"
    """

    def __init__(self):
        """
        Конструктор
        """
        LexicalParserException.__init__(self, "Операция не поддерживается для данных значений")
