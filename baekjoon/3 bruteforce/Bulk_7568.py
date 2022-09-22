import sys
input = sys.stdin.readline

n = int(input())
lst = []

for _ in range(n):
    w, h = map(int, input().split())
    lst.append((w, h))
    
for l in lst:
    r = 1
    
    for m in lst:
        if l[0] < m[0] and l[1] < m[1]:
            r += 1
            
    print(r, end=' ')