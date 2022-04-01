import sys
input = sys.stdin.readline

class queue():
    f = 0
    l = 0
    q_list = []

    def __init__(self, n):
        self.q_list = [0 for i in range(n)]

    def push(self, num):
        self.q_list[self.l] = num
        self.l += 1
    
    def pop(self):
        if self.f == self.l:
            return -1
        result = self.q_list[self.f]
        self.f += 1
        return result
    
    def size(self):
        return self.l - self.f

    def empty(self):
        if self.f == self.l:
            return 1
        return 0

    def front(self):
        if self.f == self.l:
            return -1
        return self.q_list[self.f]

    def back(self):
        if self.f == self.l:
            return -1
        return self.q_list[self.l-1]


n = int(input())
q = queue(n)

for i in range(n):
    order = input().split()

    if order[0] == 'push':
        q.push(int(order[1]))
    elif order[0] == 'pop':
        print(q.pop())
    elif order[0] == 'size':
        print(q.size())
    elif order[0] == 'empty':
        print(q.empty())
    elif order[0] == 'front':
        print(q.front())
    elif order[0] == 'back':
        print(q.back())