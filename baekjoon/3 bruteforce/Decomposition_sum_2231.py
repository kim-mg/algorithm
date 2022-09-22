import sys
input = sys.stdin.readline

n = int(input())

m = n
for _ in str(n):
    m -= 9
    
if m < 0 :
    m = 0

while m < n:
    tmp = m
    for a in str(m):
        tmp += int(a)
    if tmp == n:
        print(m)
        break
    m += 1

if m >= n:
    print(0)