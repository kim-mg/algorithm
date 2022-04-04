import sys
input = sys.stdin.readline

# ==================================================
# DP
# LIS(Longest Increasing Subsequence)
def solution(l, n):
	s = [1] * n
	for i in range(1, n):
		for j in range(i):
			if l[i] > l[j]:
				s[i] = max(s[i], s[j]+1)

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

def solution_2(l, n):
	s = [l[0]]
	s_len = 1
	for i in range(1, n):
		if l[i] > s[-1]:
			s.append(l[i])
			s_len += 1
		else:
			idx = bs(0, s_len-1, l[i], s)
			s[idx] = l[i]
	return s_len

if __name__ == "__main__":
	n = int(input())
	lst = list(map(int, input().split()))
	print(solution_2(lst, n))
