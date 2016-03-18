from Token.Token import Token


class OperatorToken(Token):
    """
    Лексема "Оператор"
    """

    def __init__(self, p_text):
        """
        Конструктор
        :param p_text: Текст
        """
        Token.__init__(self, p_text)
