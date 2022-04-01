# list append, pop만 사용가능. len, list[-1] 사용 x
# class를 이용해봐라
import sys
input = sys.stdin.readline


class Stack:
    _top = 0

    def __init__(self):
        self.stack_list = []

    def pop(self):
        if (self._top == 0):
            return -1
        num = self.stack_list[self._top-1]
        del self.stack_list[self._top-1]
        self._top -= 1
        return num

    def push(self, n):
        self.stack_list.append(n)
        self._top = self._top + 1

    def top(self):
        if self._top == 0:
            return -1
        return self.stack_list[self._top-1]

    def empty(self):
        if (self._top == 0):
            return 1
        else:
            return 0

    def size(self):
        return self._top


stack = Stack()
n = int(input())

for i in range(n):
    command = input().split()

    if (command[0] == 'push'):
        stack.push(command[1])
    elif command[0] == 'pop':
        print(stack.pop())
    elif command[0] == 'top':
        print(stack.top())
    elif command[0] == 'size':
        print(stack.size())
    elif command[0] == 'empty':
        print(stack.empty())
