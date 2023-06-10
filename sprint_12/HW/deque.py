# ID: 87543222

class SizeError(Exception):
    pass


class Deque():
    """Дек с ограниченным размером max_size"""
    def __init__(self, max_size: int) -> None:
        self.__deque = [None] * max_size
        self.__max_size = max_size
        self.__head = 0
        self.__tail = 0
        self.__deque_size = 0

    def push_back(self, value: int) -> None:
        if self.__deque_size == self.__max_size:
            raise SizeError
        self.__deque[self.__tail] = value
        self.__tail = (self.__tail + 1) % self.__max_size
        self.__deque_size += 1

    def push_front(self, value: int) -> None:
        if self.__deque_size == self.__max_size:
            raise SizeError
        self.__deque[self.__head - 1] = value
        self.__head = (self.__head - 1) % self.__max_size
        self.__deque_size += 1

    def pop_front(self) -> int:
        if not self.__deque_size:
            raise SizeError
        value = self.__deque[self.__head]
        self.__deque[self.__head] = None
        self.__head = (self.__head + 1) % self.__max_size
        self.__deque_size -= 1
        return value

    def pop_back(self) -> int:
        if not self.__deque_size:
            raise SizeError
        value = self.__deque[self.__tail - 1]
        self.__deque[self.__tail - 1] = None
        self.__tail = (self.__tail - 1) % self.__max_size
        self.__deque_size -= 1
        return value


def main():
    count_cmd = int(input())
    max_size = int(input())
    deque = Deque(max_size)
    for i in range(count_cmd):
        command = input().split()
        try:
            result = getattr(deque, command.pop(0))(*command)
            if result:
                print(result)
        except SizeError:
            print('error')


if __name__ == '__main__':
    main()
