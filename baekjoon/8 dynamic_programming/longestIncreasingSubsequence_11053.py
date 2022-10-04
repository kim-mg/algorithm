import sys
input = sys.stdin.readline

# LIS(Longest Increasing Subsequence)
# ==================================================
# DP
def solution(l, n):
	s = [1] * n
	for i in range(1, n):
		for j in range(i):
			if l[i] > l[j]:
				s[i] = max(s[i], s[j]+1)
	print(s)
	return max(s)

# ==================================================
# Binary Search
def bs(l, r, x, s):
	while l<=r:
		m = (l+r)//2
		if s[m] >= x:
			r = m - 1
		else:
			l = m + 1
	return l

def solution2(l, n):
	s = [l[0]]
	s_len = 1
	for i in range(1, n):
		if l[i] > s[-1]:
			s.append(l[i])
			s_len += 1
		else:
			idx = bs(0, s_len-1, l[i], s)
			s[idx] = l[i]
		print(s)
	return s_len

import time

if __name__ == "__main__":
	n = int(input())
	lst = list(map(int, input().split()))
	s = time.time()
	print(solution(lst, n))
	print(int((time.time() - s) * 1000), "ms")