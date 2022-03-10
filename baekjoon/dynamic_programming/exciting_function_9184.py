import sys
input = sys.stdin.readline

def dp_w(a, b, c):
    tup = (a, b, c)
    if tup not in dp_dict:
        if a <= 0 or b <= 0 or c <= 0:
            rst = dp_dict[tup] = 1
            return rst
        if a > 20 or b > 20 or c > 20:
            return dp_w(20, 20, 20)
        if a < b and b < c:
            dp_dict[tup] = dp_w(a, b, c-1) + dp_w(a, b-1, c-1) - dp_w(a, b-1, c)
            return dp_dict[tup]
        dp_dict[tup] = dp_w(a-1, b, c) + dp_w(a-1, b-1, c) + dp_w(a-1, b, c-1) - dp_w(a-1, b-1, c-1)
        return dp_dict[tup]
    else:
        return dp_dict[tup]

dp_dict = {}

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    rst = dp_w(a, b, c)
    print(f"w({a}, {b}, {c}) =", rst)

#############################################################
# another

import sys

reg = [[[-1] * 21 for _ in range(21)] for _ in range(21)]

def w(a, b, c):
    global reg
    
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if reg[a][b][c] != -1:
        return reg[a][b][c]
    if a < b < c:
        reg[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return reg[a][b][c]

    reg[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    return reg[a][b][c]

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == -1:
        break

    print("w(%d, %d, %d) = %d" % (a, b, c, w(a, b, c)))
