import sys
input = sys.stdin.readline

n = int(input())
array = []

for _ in range(n):
    x, y = map(int, input().split())
    array.append([x, y])

for l in sorted(array, key= lambda x: (x[0], x[1])):
    print(l[0], l[1])

###################################################################
# best

import sys

n = int(input())

li = [sys.stdin.readline() for _ in range(n)]
li.sort(key=lambda x: tuple(map(int, x.split())))

print(''.join(li))