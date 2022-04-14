import sys
input = sys.stdin.readline

def solution_1(x):
	s = [0] * (x + 1)
	for i in range(2, x + 1):
		s[i] = s[i - 1] + 1
		if i % 3 == 0:
			s[i] = min(s[i], s[i // 3] + 1)
		if i % 2 == 0:
			s[i] = min(s[i], s[i // 2] + 1)
	print(s[x])

# ====================================================
# best

def dp(n):
	if n in s2:
		return s2[n]
	m = 1 + min(dp(n//2) + n%2, dp(n//3) + n%3)
	s2[n] = m
	return m

def solution_2(x):
	print(dp(x))

if __name__ == "__main__":
	x = int(input())
	s2 = {1:0,2:1}
	solution_2(x)