import sys
input = sys.stdin.readline

def binary_search(left, right, val, l):
	while left <= right:
		mid = (right + left) // 2
		if val > l[mid]:
			left = mid + 1
		else:
			right = mid - 1
	return left

def solution():
	n = int(input())
	l = list(map(int, input().split()))

	s = [1, l[0]]
	for i in range(1, n):
		if s[-1] < l[i]:
			s.append(l[i])
			s[0] += 1
		elif s[-1] > l[i]:
			lb = binary_search(1, s[0], l[i], s)
			s[lb] = l[i]
	print(s[0])

##################################################################3
# effecient
from bisect import bisect_left

def solution2():
	n = int(input())
	l = list(map(int, input().split()))

	s = [l[0]]
	cnt = 1
	for i in range(1, n):
		if s[-1] < l[i]:
			s.append(l[i])
			cnt += 1
		elif s[-1] > l[i]:
			s[bisect_left(s, l[i])] = l[i]
	print(cnt)

if __name__ == "__main__":
	# solution()
	solution2()