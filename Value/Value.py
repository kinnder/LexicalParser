from Exception.UnSupportedOperation import UnSupportedOperation


class Value(object):
    """
    Значение
    """
    data = ""

    def __init__(self, p_data=""):
        """
        Конструктор
        :param p_data Данные
        """
        self.data = p_data

    def __str__(self):
        """
        Преобразование в строку
        :return Строковое представление
        """
        return str(self.data)

    def subtract(self, p_value):
        """
        Операция "Вычитание"
        :param p_value: Вычитаемое
        :return: Результат операции
        """
        raise UnSupportedOperation()

    def add(self, p_value):
        """
        Операция "Сложение"
        :param p_value: Слагаемое
        :return: Результат операции
        """
        raise UnSupportedOperation()

    def multiply(self, p_value):
        """
        Операция "Умножение"
        :param p_value: Множитель
        :return: Результат операции
        """
        raise UnSupportedOperation()

    def divide(self, p_value):
        """
        Операция "Деление"
        :param p_value: Делитель
        :return: Результат операции
        """
        raise UnSupportedOperation()

    def modulo(self, p_value):
        """
        Операция "Деление с остатком"
        :param p_value: Делитель
        :return: Результат операции
        """
        raise UnSupportedOperation

    def power(self, p_value):
        """
        Операция "Возведение в степень"
        :param p_value: Показатель степени
        :return: Результат операции
        """
        raise UnSupportedOperation

    def minus_sign(self):
        """
        Операция "Унарный минус"
        :return: Результат операции
        """
        raise UnSupportedOperation
