import sys
input = sys.stdin.readline

def string_to_ascii(s):
    rst = []
    for a in s:
        rst.append(ord(a))
    return rst

n = int(input())
array = set(list(input().rstrip() for _ in range(n)))

sorted_array = sorted(array, key=lambda x: (len(x), string_to_ascii(x)))

for s in sorted_array:
    print(s)

###########################################################################
# best

import sys
input = sys.stdin.readline

n = int(input())
array = set()
for _ in range(n):
    array.add(input().rstrip())
array = list(array)
print(array)
# 문자열을 가진 리스트를 sort()하면 기본값은 사전순으로 정렬
array.sort()
print(array)
array.sort(key=lambda x: len(x))
print("\n".join(array))