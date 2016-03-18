from Value.Value import Value
from Exception.DivisionByZero import DivisionByZero


class DigitValue(Value):
    """
    Численное значение
    """

    def __init__(self, p_data):
        """
        Конструктор
        :param p_data: Данные
        """
        Value.__init__(self, p_data)

    def to_double(self):
        """
        Преобразование в число
        :return: Численное представление
        """
        try:
            return float(self.data)
        except ValueError:
            raise SyntaxError

    def subtract(self, p_value):
        """
        Операция "Вычитание
        :param p_value: Вычитаемое
        :return: Результат операции
        """
        return DigitValue(self.to_double() - p_value.to_double())

    def add(self, p_value):
        """
        Операция "Сложение"
        :param p_value: Слагаемое
        :return: Результат операции
        """
        return DigitValue(self.to_double() + p_value.to_double())

    def multiply(self, p_value):
        """
        Операция "Умножение
        :param p_value: Множитель
        :return: Результат операции
        """
        return DigitValue(self.to_double() * p_value.to_double())

    def divide(self, p_value):
        """
        Операция "Деление"
        :param p_value: Делитель
        :return: Результат операции
        """
        if p_value.to_double() == 0:
            raise DivisionByZero
        return DigitValue(self.to_double() / p_value.to_double())

    def modulo(self, p_value):
        """
        Операция "Деление с остатком"
        :param p_value: Делитель
        :return: Результат операции
        """
        if p_value.to_double() == 0:
            raise DivisionByZero
        return DigitValue(self.to_double() % p_value.to_double())

    def power(self, p_value):
        """
        Операция "Возведение в степень"
        :param p_value: Показатель степени
        :return: Результат операции
        """
        if p_value.to_double() == 0:
            return DigitValue(1.0)
        result = exponential = self.to_double()
        for i in range(1, int(p_value.to_double()), 1):
            result *= exponential
        return DigitValue(result)

    def minus_sign(self):
        """
        Операция "Унарный минус"
        :return: Результат операции
        """
        return DigitValue(-self.to_double())
