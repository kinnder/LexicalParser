from Exception.LexicalParserException import LexicalParserException


class UnBalancedBrackets(LexicalParserException):
    """
    Исключение "Дисбаланс скобок"
    """

    def __init__(self):
        """
        Конструктор
        """
        LexicalParserException.__init__(self, "Дисбаланс скобок")
