# mine
import sys
input = sys.stdin.readline

def recursive_stars(n):
    if n == 3:
        m[1][:3] = ['*', ' ', '*']
        m[0][:3] = ['*'] * 3
        m[2][:3] = ['*'] * 3
        return 
    
    d = n // 3
    recursive_stars(d)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(d):
                m[d*i+k][d*j:d*(j+1)] = m[k][:d]

n = int(input())
m = [[' ' for _ in range(n)] for _ in range(n)]

recursive_stars(n)

for i in m:
    for j in i:
        print(j, end='')
    print()


###################################################################
print('\n' + '---------------------------------------------------' + '\n')
# best

def sol(n):
    if n<2: return ['*']
    d = sol(n//3)
    c = [i*3 for i in d]
    return c + [i+ ' '*(n//3) + i for i in d] + c

print('\n'.join(sol(n)))