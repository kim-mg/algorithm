# Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다. 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.

# import sys
# input = sys.stdin.readline

# a = int(input())
# b = int(input())

# a = int(input())

# a, b = map(int, input().split())

# n = int(input())

import time
import math
import itertools
import sys
input = sys.stdin.readline

n = int(input())
padovan_lst = [0, 1, 1, 1] + [0] * 97

for i in range(4, 101):
    padovan_lst[i] = padovan_lst[i-2] + padovan_lst[i-3]

for _ in range(n):
    m = int(input())
    print(padovan_lst[m])