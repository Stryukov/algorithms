class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        return False

    def size(self):
        return len(self.items)


def is_correct_bracket_seq(seq):
    stack = Stack()
    brackets = {
        '(': 1,
        ')': 1,
        '[': 2,
        ']': 2,
        '{': 3,
        '}': 3,
    }
    for char in seq:
        if char in ['(', '[', '{']:
            stack.push(brackets[char])
        if char in [')', ']', '}']:
            result = stack.pop()
            if result:
                if result != brackets[char]:
                    return False
            else:
                return False

    if stack.size() > 0:
        return False
    return True


def main():
    seq = input()
    print(is_correct_bracket_seq(seq))


if __name__ == '__main__':
    main()
