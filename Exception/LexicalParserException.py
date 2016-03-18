class LexicalParserException(Exception):
    """
    Исключение синтаксического анализатора
    """
    message = ""

    def __init__(self, p_message):
        """
        Конструктор
        :param p_message: Текст сообщения
        """
        self.message = p_message

    def __str__(self):
        """
        Преобразование в строку
        :return: Строковое представление
        """
        return self.message
