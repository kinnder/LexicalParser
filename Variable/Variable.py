from Value.Value import Value


class Variable(object):
    """
    Переменная
    """

    def __init__(self, p_name=""):
        """
        Конструктор
        :param p_name: Название
        """
        self.name = p_name
        self.value = Value()
