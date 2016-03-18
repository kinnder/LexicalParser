from Variable.Variable import Variable


class VariableList(object):
    """
    Массив переменных
    """

    def __init__(self):
        """
        Конструктор
        """
        self.items = []

    def __getitem__(self, p_name):
        """
        Индексатор
        :param p_name: Имя переменной
        :return: Переменная
        """
        index = self.find(p_name)
        if index == -1:
            self.items.append(Variable(p_name))
        return self.items[index]

    def find(self, p_name):
        """
        Поиск переменной с указанным именем
        :param p_name: Имя переменной
        :return: Индекс найденной переменной или -1 в случае её отсутсвия
        """
        for i in range(0, len(self.items)):
            if self.items[i].name == p_name:
                return i
        return -1
