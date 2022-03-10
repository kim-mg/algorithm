import sys
input = sys.stdin.readline

n = int(input())
padovan_lst = [0, 1, 1, 1] + [0] * 97

for i in range(4, 101):
    padovan_lst[i] = padovan_lst[i-2] + padovan_lst[i-3]

for _ in range(n):
    m = int(input())
    print(padovan_lst[m])