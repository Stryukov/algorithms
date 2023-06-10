class SizeError(Exception):
    pass


class ListQueue:
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

        def __str__(self):
            return str(self.value)

    def __init__(self):
        self.head = None
        self.tail = None
        self.queue_size = 0

    def get(self):
        if self.queue_size == 0:
            raise SizeError
        else:
            item = self.head
            self.head = item.next
            self.queue_size -= 1
            return item.value

    def put(self, item):
        if self.queue_size == 0:
            self.head = self.Node(item)
            self.tail = self.head
        else:
            node = self.Node(item)
            self.tail.next = node
            self.tail = node
        self.queue_size += 1

    def size(self):
        return self.queue_size


def main():
    count_cmd = int(input())
    queue = ListQueue()
    for i in range(count_cmd):
        command = input().split()
        if command[0] == 'put':
            queue.put(command[1])
        if command[0] == 'get':
            try:
                print(queue.get())
            except SizeError:
                print('error')
        if command[0] == 'size':
            print(queue.size())


if __name__ == '__main__':
    main()
