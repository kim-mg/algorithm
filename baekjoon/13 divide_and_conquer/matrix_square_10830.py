import sys
input = sys.stdin.readline

def multiple(n, a, b):
	r = [[0 for _ in range(n)] for _ in range(n)]

	for row in range(n):
		for col in range(n):
			for ele in range(n):
				r[row][col] += (a[row][ele] * b[ele][col]) % 1000
			r[row][col] %= 1000
	return r

def mat_square(mat, n, k):
	if k == 1:
		for row in range(n):
			for col in range(n):
				mat[row][col] %= 1000
		return mat
	
	tmp = mat_square(mat, n, k//2)
	if k % 2:
		return multiple(n, multiple(n, tmp, tmp), mat)
	else:
		return multiple(n, tmp, tmp)

def solution():
	n, m = map(int, input().split())
	a = []
	for _ in range(n):
		a.append(list(map(int, input().split())))
	r = mat_square(a, n, m)
	line = []
	for i in range(n):
		line.append(' '.join(map(str, r[i])))
	print('\n'.join(line))

if __name__ == "__main__":
	solution()