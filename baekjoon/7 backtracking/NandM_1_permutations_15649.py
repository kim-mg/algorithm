import sys
input = sys.stdin.readline

def tracking_seq(t, n, m):
    if len(t) >= m:
        print(' '.join(map(str, t)).rstrip())
        return

    for i in range(1, n+1):
        if i in t:
            continue
        temp = t.copy()
        temp.append(i)
        tracking_seq(temp, n, m)

n, m = map(int, input().split())
table = []
tracking_seq(table, n, m)

#####################################################################
# best
import itertools
import sys
input = sys.stdin.readline

p = itertools.permutations
n, m = map(int, input().split())
array = map(str, range(1, n+1))
print('\n'.join(list(map(' '.join,p(array, m)))))