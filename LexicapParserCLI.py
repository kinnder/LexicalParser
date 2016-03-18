from Exception.LexicalParserException import LexicalParserException
from LexicalParser import LexicalParser

parser = LexicalParser()

print("Для выхода из программы введите пустое выражение")

while True:
    print("Введите выражение: ")
    expression = input()
    if expression == "":
        break
    try:
        print("Результат: " + parser.evaluate(expression).__str__())
    except LexicalParserException as exception:
        print("Ошибка: " + exception.__str__())
