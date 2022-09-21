import sys
input = sys.stdin.readline

n = int(input())
mem = []
for _ in range(n):
    mem.append(input().split())

sorted_mem = sorted(mem, key=lambda x: int(x[0]))
print("\n".join(map(lambda x: x[0] + ' ' + x[1], sorted_mem)))

####################################################################
# best

import sys
input = sys.stdin.readline

n = int(input())
mem_by_age = [[] for _ in range(200+1)]

for _ in range(n):
    l = input().split()
    mem_by_age[int(l[0])].append(l[1])

print(''.join(''.join(m) for m in mem_by_age))