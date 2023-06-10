class StackMax():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        return print('error')

    def get_max(self):
        max = None
        if self.items:
            for item in self.items:
                if max is None or item > max:
                    max = item
        return max


def main():
    num_commands = int(input())
    stack = StackMax()
    for i in range(num_commands):
        command = input()
        txt_command = command.split()[0]
        if txt_command == 'get_max':
            print(stack.get_max())
        if txt_command == 'pop':
            stack.pop()
        if txt_command == 'push':
            stack.push(int(command.split()[1]))


if __name__ == '__main__':
    main()
