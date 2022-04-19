from itertools import accumulate
import sys
input = sys.stdin.readline

def solution(n, m):
	mat = [[0] * (n+1) for _ in range(n+1)]
	r = []
	for i in range(1, n+1):
		for j, num in enumerate(map(int, input().split())):
			mat[i][j+1] = mat[i-1][j+1] + mat[i][j] + num - mat[i-1][j]
	for _ in range(m):
		x1, y1, x2, y2 = map(int, input().split())
		r.append(str(mat[x2][y2] - mat[x1-1][y2] - mat[x2][y1-1] + mat[x1-1][y1-1]))
	print('\n'.join(r))

# ========================================================
# best time
# how to use lambda a, b not c or d
def solution2(n, m):
	r = [list(accumulate(map(int, input().split()))) for _ in range(n)]
	mem = list(accumulate(r, lambda a, b: list(map(sum, zip(a, b)))))
	s = []
	for _ in range(m):
		x1, y1, x2, y2 = map(int, input().split())
		t = mem[x2-1][y2-1]
		if x1-1:
			t -= mem[x1-2][y2-1]
		if y1-1:
			t -= mem[x2-1][y1-2]
		if x1-1 and y1-1:
			t += mem[x1-2][y1-2]
		s.append(str(t))
	print('\n'.join(s))

if __name__ == "__main__":
	n, m = map(int, input().split())
	solution2(n, m)