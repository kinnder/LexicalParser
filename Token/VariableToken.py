from Token.Token import Token


class VariableToken(Token):
    """
    Лексема "Имя переменной"
    """

    def __init__(self, p_text):
        """
        Конструктор
        :param p_text: Текст
        """
        Token.__init__(self, p_text)
