import sys
input = sys.stdin.readline

def sieve(num):
    lst = [0, 0, 1] + [1, 0] * (num // 2)
    for i in range(3, round(num**0.5)+1, 2):
        if lst[i] == 1:
            lst[i*2::i] = [0] * len(lst[i*2::i])
    return lst

n = int(input())
s = sieve(10000)
for _ in range(n):
    m = int(input())
    h_m = m//2
    if h_m % 2 == 0:
        h_m += 1
    if m == 4:
        h_m = 2
    for i in range(h_m, m, 2):
        if s[i] and s[m-i]:
            print(m-i, i)
            break