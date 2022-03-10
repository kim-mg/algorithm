import sys
input = sys.stdin.readline

def count_diff(s, c):
    rst = 0

    for a, b in zip(s, c):
        if a != b:
            rst += 1
    return rst

n, m = map(int, input().split())
lst = []

for _ in range(n):
    lst.append(input().rstrip())

x = n - 8
rst = 32
check = ['WBWBWBWB', 'BWBWBWBW']
while x >= 0:
    y = m - 8
    while y >= 0:
        b = 0
        w = 0
        b_i = 1
        w_i = 0
        for i in range(x, x+8):
            b += count_diff(lst[i][y:y+8], check[b_i])
            w += count_diff(lst[i][y:y+8], check[w_i])
            b_i = (b_i + 1) % 2
            w_i = (w_i + 1) % 2
        if rst > min(b, w):
            rst = min(b, w)
        y -= 1
    x -= 1
print(rst)

#################################################################
# best

import sys
from itertools import accumulate as acc
input = sys.stdin.readline
n, m = map(int, input().split())
y = [[0]*(m+1)]
for i in range(n):
    ac = [0]
    ac.extend(acc([((s=='W')+i+j) % 2 for j, s in enumerate(input().rstrip())]))
    y.append([k + j for k, j in zip(ac, y[-1])])
    
res = 32
for i in range(n-7):
    for j in range(m-7):
        u = y[i+8][j+8]-y[i+8][j]-y[i][j+8]+y[i][j]
        res = min(res, u, 64-u)
print(res)