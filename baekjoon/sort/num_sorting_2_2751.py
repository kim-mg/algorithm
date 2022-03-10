import sys
input = sys.stdin.readline

n = int(input())
lst = []

for _ in range(n):
    lst.append(int(input()))

r_lst = sorted(lst)

for i in r_lst:
    print(i)