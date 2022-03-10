import itertools
import sys
input = sys.stdin.readline

c = itertools.combinations

n, m = map(int, input().split())
array = [str(i) for i in range(1, n+1)]
print('\n'.join(list(map(' '.join, c(array, m)))))