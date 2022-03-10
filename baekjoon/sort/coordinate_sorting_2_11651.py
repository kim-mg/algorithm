import sys
input = sys.stdin.readline

n = int(input())
array = []

for _ in range(n):
    x, y = map(int, input().split())
    array.append([x, y])

for l in sorted(array, key= lambda x: (x[1], x[0])):
    print(l[0], l[1])

###################################################################
# best

import sys

n = int(input())

li = [sys.stdin.readline() for _ in range(n)]
li.sort(key=lambda x: (int(x.split()[1]), int(x.split()[0])))

print(''.join(li))