# ID: 87548284
from operator import add, sub, floordiv, mul


class Stack:
    def __init__(self) -> None:
        self.__items = []

    def push(self, item: int) -> None:
        self.__items.append(item)

    def pop(self) -> int:
        return self.__items.pop()


def calculate(exp: str) -> int:
    """Вычисляет значения выражения, 
    записанного в обратной польской нотации.
    """
    stack = Stack()
    operator = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': floordiv,
    }
    for elem in exp:
        try:
            stack.push(int(elem))
        except ValueError:
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.push(operator[elem](operand1, operand2))
    return stack.pop()


def main():
    exp = input().split()
    print(calculate(exp))


if __name__ == '__main__':
    main()
