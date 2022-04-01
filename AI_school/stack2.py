import sys
input = sys.stdin.readline
 
 
def process_stack(command):
 
    if command[0] == "push":
        storage.append(int(command[1]))
    elif command[0] == "pop":
        if not storage:
            print(-1)
        else:
            print(storage.pop())
    elif command[0] == "size":
        n = 0
        for _ in storage:
            n += 1
        print(n)
    elif command[0] == "empty":
        if not storage:
            print(1)
        else:
            print(0)
    elif command[0] == "top":
        if not storage:
            print(-1)
        else:
            m = 0
            for _ in storage:
                m += 1
            print(storage[m-1])
 
 
n = int(input())
storage = []
 
for _ in range(n):
    command = input().split()
    process_stack(command)