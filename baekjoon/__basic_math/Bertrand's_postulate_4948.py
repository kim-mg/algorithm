import sys
input = sys.stdin.readline

def sieve(num):
    lst = [1 for _ in range((num+1)//2)]
    for i in range(3, round(num**0.5)+1, 2):
        if lst[i // 2] == 1 :
            k = i * i
            for j in range(k//2, (num+1)//2, i):
                lst[j] = 0
    return lst

def get_prime_num(num):
    lst = sieve(num)
    rst = [2]
    for i in range(1, len(lst)):
        if lst[i] == 1:
            rst.append(i*2 + 1)
    return rst

def search(p_lst, num):
    f, r = 0, len(p_lst)-1
    while f <= r:
        m = (f+r)//2

        if p_lst[m] > num:
            r = m-1
        else:
            f = m+1
    return f

s = get_prime_num(123456*2)
while True:
    n = int(input())
    
    if n == 0:
        break
    elif n == 1:
        print(1)
        continue

    print(search(s,2*n) - search(s,n))