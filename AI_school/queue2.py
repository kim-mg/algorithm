import sys
input = sys.stdin.readline

class process_queue:
    q_sto = []
    f = 0
    l = 0

    def __init__(self, n):
        self.q_sto = [0 for i in range(n)]

    def push(self, n):
        self.q_sto[self.l] = n
        self.l += 1

    def pop(self):
        if self.f == self.l:
            return -1
        res = self.q_sto[self.f]
        self.f += 1
        return res

    def size(self):
        return self.l - self.f

    def empty(self):
        if self.f == self.l:
            return 1
        else:
            return 0

    def front(self):
        if self.f == self.l:
            return -1
        return self.q_sto[self.f]

    def back(self):
        if self.f == self.l:
            return -1
        return self.q_sto[self.l-1]

n = int(input())
q = process_queue(n)

for _ in range(n):
    command = input().split()

    if command[0] == "push":
        q.push(command[1])
    elif command[0] == "pop":
        print(q.pop())
    elif command[0] == "size":
        print(q.size())
    elif command[0] == "empty":
        print(q.empty())
    elif command[0] == "front":
        print(q.front())
    elif command[0] == "back":
        print(q.back())
    
    