import threading
import time


class Stack:
    def __init__(self):
        self.data = [-1] * 5
        self.pointer = -1

    def push(self, x):
        global event
        while self.pointer == len(self.data) - 1:
            event.wait()
        event.set()
        self.pointer += 1
        self.data[self.pointer] = x

    def pop(self):
        global event
        while self.pointer == -1:
            event.wait()
        event.set()
        x = self.data[self.pointer]
        self.pointer -= 1
        return x


def producer():
    global stack
    for i in range(10):
        stack.push(i)
        print('生产：%d' % i)
        time.sleep(1)


def consumer():
    global stack
    for i in range(10):
        x = stack.pop()
        print('消费：%d' % x)
        time.sleep(1)


if __name__ == '__main__':
    stack = Stack()
    event = threading.Event()

    t1 = threading.Thread(target=producer)
    t1.start()
    t2 = threading.Thread(target=consumer)
    t2.start()
