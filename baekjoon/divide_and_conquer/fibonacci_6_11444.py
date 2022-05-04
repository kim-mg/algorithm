import sys
input = sys.stdin.readline

def mat_multiple(a, b):
	m = [[0, 0], [0, 0]]

	for r in range(2):
		for c in range(2):
			for e in range(2):
				m[r][c] += a[r][e] * b[e][c]
			m[r][c] %= 1000000007
	return m

def mat_square(m, k):
	if k == 1:
		for r in range(2):
			for c in range(2):
				m[r][c] %= 1000000007
		return m

	tmp = mat_square(m, k//2)
	if k % 2:
		return mat_multiple(mat_multiple(tmp, tmp), m)
	else:
		return mat_multiple(tmp, tmp)

def solution():
	n = int(input())
	a = [[1, 1], [1, 0]]
	r = mat_square(a, n)
	v = r[1][0]
	print(v)

if __name__ == "__main__":
	solution()