import sys
input = sys.stdin.readline

class queue:
    f = 0
    r = 0
    q_list = []

    def __init__(self, n):
        if (n>=1) and (n<=10000):
            self.num = n
            self.q_list = [0 for i in range(n)]
        else:
            print("n은 1이상 10,000이하의 정수를 입력해주세요")

    def push(self, n):
        self.q_list[self.r] = n
        self.r += 1
    
    def pop(self):
        if self.r == 0:
            return -1
        else:
            result = self.q_list[self.f]
            self.f += 1
            if self.f >= self.r:
                self.f = 0
                self.r = 0
            return result

    def size(self):
        return self.r

    def empty(self):
        if self.r == 0:
            return 1
        else:
            return 0

    def front(self):
        if self.r == 0:
            return -1
        else:
            return self.q_list[self.f]

    def back(self):
        if self.r == 0:
            return -1
        else:
            return self.q_list[self.r - 1]

n = int(input())
q = queue(n)

for _ in range(n):

    cmd = input().split()
    
    if cmd[0] == "push":
        q.push(int(cmd[1]))
    elif cmd[0] == "pop":
        print(q.pop())
    elif cmd[0] == "size":
        print(q.size())
    elif cmd[0] == "empty":
        print(q.empty())
    elif cmd[0] == "front":
        print(q.front())
    elif cmd[0] == "back":
        print(q.back())

