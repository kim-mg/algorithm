import sys
input = sys.stdin.readline

def solution():
	n, m = map(int, input().split())
	a = []
	b = []

	for _ in range(n):
		a.append(list(map(int, input().split())))
	
	nn, mm = map(int, input().split())
	r = [[0 for _ in range(mm)] for _ in range(n)]
	
	for _ in range(nn):
		b.append(list(map(int, input().split())))
	
	for i in range(n):
		for j in range(mm):
			for k in range(m):
				r[i][j] += a[i][k] * b[k][j]
	
	line = []
	for i in range(n):
		line.append(' '.join(list(map(str, r[i]))))
	print('\n'.join(line))

if __name__ == "__main__":
	solution()
