import sys
input = sys.stdin.readline

# DP
# ==================================================
# longest increase subsequence & longest decrease subsequence
def solution(l, n):
	s_incr = [1] * n
	s_decr = [1] * n
	for i in range(1, n):
		for j in range(i):
			if l[i] > l[j]:
				s_incr[i] = max(s_incr[i], s_incr[j]+1)
	for i in range(n-2, -1, -1):
		for j in range(n-1, i, -1):
			if l[i] > l[j]:
				s_decr[i] = max(s_decr[i], s_decr[j]+1)
	ans = [0] * n
	m = ans[0]
	for i in range(n):
		ans[i] = s_incr[i] + s_decr[i]
		if ans[i] > m:
			m = ans[i]
	return m - 1

# ==================================================
# binary search

def bs(l, r, x, s):
	while l<=r:
		m = (l + r) // 2
		if s[m] >= x:
			r = m - 1
		else:
			l = m + 1
	return l

def solution_2(l, n):
	s_incr = [l[0]]
	s_incr_size = [1] * n
	s_decr_size = [1] * n
	for i in range(1, n):
		if l[i] > s_incr[-1]:
			s_incr.append(l[i])
			s_incr_size[i] = len(s_incr)
		else:
			idx = bs(0, len(s_incr) - 1, l[i], s_incr)
			s_incr[idx] = l[i]
			s_incr_size[i] = idx + 1
	l.reverse()
	s_decr = [l[0]]
	for j in range(1, n):
		if l[j] > s_decr[-1]:
			s_decr.append(l[j])
			s_decr_size[j] = len(s_decr)
		else:
			idx = bs(0, len(s_decr) - 1, l[j], s_decr)
			s_decr[idx] = l[j]
			s_decr_size[i] = idx + 1
	s_size = [1] * n
	for i in range(n):
		s_size[i] = s_incr_size[i] + s_decr_size[n - (i + 1)]
	return max(s_size) - 1

if __name__ == "__main__":
	n = int(input())
	lst = list(map(int, input().split()))
	print(solution_2(lst, n))
