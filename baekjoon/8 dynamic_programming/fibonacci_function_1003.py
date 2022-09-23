import sys
input = sys.stdin.readline

def fibonacci(n):
    global a, b
    if n == 0:
        a += 1
        return 0
    if n == 1:
        b += 1
        return 1
    if n not in fibo_dict:
        rst = fibonacci(n-1) + fibonacci(n-2)
        fibo_dict[n] = [a, b]
        return rst
    else:
        lst = fibo_dict[n]
        a += lst[0]
        b += lst[1]
        return fibo_dict[n][1]

n = int(input())
fibo_dict = {}

for _ in range(n):
    i = int(input())
    a, b = 0, 0
    fibonacci(i)
    print(a, b)

##########################################################
# best
import sys

n = int(input())
dp = [[1,0], [0,1]]
q = [int(sys.stdin.readline()) for _ in range(n)]

for i in range(2, max(q)+1):
    dp.append([dp[i-2][0] + dp[i-1][0], dp[i-2][1] + dp[i-1][1]])
for i in q:
    print(dp[i][0], dp[i][1])