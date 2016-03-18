from Value.Value import Value


class Token(object):
    """
    Лексема
    """
    text = ""

    @staticmethod
    def copy(p_token):
        """
        Копирование
        :param p_token: Копируемая лексема
        :return: Результат копирования
        """
        return Token(p_token.text)

    def __init__(self, p_text=""):
        """
        Конструктор
        :param p_text: Текст
        """
        self.text = p_text

    def is_empty(self):
        """
        Предикат "Является пустой
        """
        return self.text == ""

    def is_assign(self):
        """
        Предикат "Является оператором ="
        """
        return self.text == "="

    def is_plus(self):
        """
        Предикат "Является оператором +"
        """
        return self.text == "+"

    def is_minus(self):
        """
        Предикат "Является оператором -"
        """
        return self.text == "-"

    def is_multiplication(self):
        """
        Предикат "Является оператором *"
        """
        return self.text == "*"

    def is_division(self):
        """
        Предикат "Является оператором /"
        """
        return self.text == "/"

    def is_modulo(self):
        """
        Предикат "Является оператором %"
        """
        return self.text == "%"

    def is_power(self):
        """
        Предикат "Является оператором ^"
        """
        return self.text == "^"

    def is_opening_bracket(self):
        """
        Предикат "Является оператором ("
        """
        return self.text == "("

    def is_closing_bracket(self):
        """
        Предикат "Является оператором )"
        """
        return self.text == ")"

    def to_value(self):
        """
        Преобразование в значение
        :return: Представление в виде значения
        """
        return Value(self.text)

    def put_as_first_in_string(self, p_expression):
        """
        Возрвращение лексемы в строку
        Текст лексемы вставляется в начало строки
        :param p_expression: Строка
        :return: Результирующая строка
        """
        return self.text + " " + p_expression
