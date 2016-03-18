from Value.Value import Value


class StringValue(Value):
    """
    Строковое значение
    """

    def __init__(self, p_data):
        """
        Конструктор
        :param p_data: Данные
        """
        Value.__init__(self, p_data)

    def add(self, p_value):
        """
        Операция "Сложение"
        :param p_value: Слагаемое
        :return: Результат операции
        """
        return StringValue(self.data + p_value.data)
