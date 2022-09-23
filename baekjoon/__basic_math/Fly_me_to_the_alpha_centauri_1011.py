import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    s = y - x
    cnt = 0
    m = 1
    sum = 0

    while sum < s:
        cnt += 1
        sum += m
        if cnt % 2 == 0:
            m += 1

    print(cnt)