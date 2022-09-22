import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = list(map(int, input().split()))

max_n = 0
f = 1
for i in range(n):
    if f == 0:
        break
    for j in range(i+1, n):
        if f == 0:
            break
        for k in range(j+1,n):
            s = l[i] + l[j] + l[k]
            if s == m:
                max_n = s
                f = 1
                break
            elif s < m and s > max_n:
                max_n = s
print(max_n)