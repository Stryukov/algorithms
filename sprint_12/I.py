class MyQueueSized:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_n = max_size
        self.head = 0
        self.tail = 0
        self.queue_size = 0

    def push(self, item):
        if self.queue_size != self.max_n:
            self.queue[self.tail] = item
            self.tail = (self.tail + 1) % self.max_n
            self.queue_size += 1
        else:
            return 'error'

    def pop(self):
        if self.queue_size:
            item = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.max_n
            self.queue_size -= 1
            return item
        else:
            return None

    def peek(self):
        if self.queue_size:
            return self.queue[self.head]
        else:
            return None

    def size(self):
        return self.queue_size


def main():
    count_cmd = int(input())
    max_size = int(input())
    queue = MyQueueSized(max_size)
    for i in range(count_cmd):
        command = input().split()
        if command[0] == 'push':
            result = queue.push(command[1])
            if result:
                print(result)
        if command[0] == 'pop':
            print(queue.pop())
        if command[0] == 'peek':
            print(queue.peek())
        if command[0] == 'size':
            print(queue.size())


if __name__ == '__main__':
    main()
