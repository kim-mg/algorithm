import sys
input = sys.stdin.readline

n = input().rstrip()
l = [0] * 10

for i in n:
    l[int(i)] += 1

r = ''
for i in range(len(l)-1, -1, -1):
    for _ in range(l[i]):
        r += str(i)

print(r)