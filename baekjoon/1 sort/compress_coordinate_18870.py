import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
dict = dict(list([x, i] for i, x in enumerate(sorted(set(array)))))

for i in range(len(array)):
    array[i] = dict[array[i]]

print(' '.join(map(str, array)).rstrip())

##################################################################
# best - 나와 비슷한 방법

import sys

count = sys.stdin.readline()
numbers = list(map(int, sys.stdin.readline().split()))

keys = sorted(set(numbers))
location = dict(zip(keys, map(str, range(len(keys)))))

sys.stdout.write(' '.join([location[i] for i in numbers]))