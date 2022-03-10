import sys
input = sys.stdin.readline

def hanoi(n, f, t, s):
    if n == 1:
        print(f, t)
        return

    hanoi(n-1, f, s, t)
    print(f, t)
    hanoi(n-1, s, t, f)

n = int(input())

# print(2**n - 1)
# hanoi(n, 1, 3, 2)

######################################################
# best - use cache

cache = {}
def hanoi_cache(n, f, t):
    if n == 1:
        return f'{f} {t}\n'
    if (n, f, t) in cache:
        return cache[(n, f, t)]
    
    s = 6 - f - t
    tmp = [hanoi_cache(n-1, f, s), f'{f} {t}\n', hanoi_cache(n-1, s, t)]
    cache[(n, f, t)] = ''.join(tmp)
    return cache[(n, f, t)]

print(2**n - 1)
print(hanoi_cache(n, 1, 3))