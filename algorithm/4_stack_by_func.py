def proc_stack(l, s, command):
    com = command[0]
    if len(command) > 1:
        num = int(command[1])
        
    if com == "push":
        l.append(num)
        s += 1
    if com == "pop":
        if s:
            print(l.pop())
            s -= 1
        else:
            print(-1)
    if com == "size":
        print(s)
    if com == "empty":
        if s == 0:
            print(1)
        else:
            print(0)
    if com == "top":
        if s:
            print(l[s-1])
        else:
            print(-1)
    return [l, s]

n = int(input())

l = []
size = 0

for _ in range(n):
    command = input().split(" ")
    l, size = proc_stack(l, size, command)