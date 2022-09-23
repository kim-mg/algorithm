import sys
input = sys.stdin.readline

n = int(input())
bi_lst = [0, 1, 2] + [0] * (n-2)

if n > 2:
    for i in range(3, n+1):
        bi_lst[i] = (bi_lst[i-1] + bi_lst[i-2])%15746
print(bi_lst[n])

###############################################################
# best

import sys
input = sys.stdin.readline

n = int(input())
bi_dict = {
    0:0,
    1:1
}
mod = 15746

def dp(i):
    if i in bi_dict:
        return bi_dict[i]
    else:
        if i%2 == 0:
            a = dp(i//2 -1)%mod
            b = dp(i//2)%mod
            f = ((2*a+b)*b)%mod
            print(i, a, b, f)
        else:
            f = (dp((i+1)//2)%mod)**2 + (dp((i-1)//2)%mod)**2
            print(i, f)
        bi_dict[i] = f%mod
        return f%mod
print(dp(n+1))
print(bi_dict)