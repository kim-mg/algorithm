import sys
input = sys.stdin.readline


class Queue:
    f = 0
    r = 0
    q_list = []

    def __init__(self, n):
        self.num = n
        self.q_list = [0 for i in range(n)]

    def pop(self):
        if (self.r == self.f):
            return -1
        result = self.q_list[self.f]
        self.f += 1
        return result

    def push(self, n):
        self.q_list[self.r] = n
        self.r += 1

    def size(self):
        return self.r - self.f

    def empty(self):
        if (self.r == self.f):
            return 1
        else:
            return 0

    def front(self):
        if (self.r == self.f):
            return -1
        return self.q_list[self.f]

    def back(self):
        if (self.r == self.f):
            return -1
        return self.q_list[self.r-1]


n = int(input())

q = Queue(n)
for i in range(n):
    command = input().split()

    if (command[0] == 'push'):
        q.push(command[1])
    elif command[0] == 'pop':
        print(q.pop())
    elif command[0] == 'size':
        print(q.size())
    elif command[0] == 'empty':
        print(q.empty())
    elif command[0] == 'front':
        print(q.front())
    elif command[0] == 'back':
        print(q.back())
