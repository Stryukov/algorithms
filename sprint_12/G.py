class StackMaxEffective():
    def __init__(self):
        self.items = []

    def push(self, value):
        if self.items:
            item = (value, max(self.items[-1][1], value))
        else:
            item = (value, value)
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        return print('error')

    def get_max(self):
        max = None
        if self.items:
            max = self.items[-1][1]
        return max


def main():
    num_commands = int(input())
    stack = StackMaxEffective()
    for i in range(num_commands):
        command = input().split()
        if command[0] == 'get_max':
            print(stack.get_max())
        if command[0] == 'pop':
            stack.pop()
        if command[0] == 'push':
            stack.push(int(command[1]))


if __name__ == '__main__':
    main()
