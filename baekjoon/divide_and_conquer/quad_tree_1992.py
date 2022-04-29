import sys
input = sys.stdin.readline

def recur(l, x, y, n, r):
	if n == 0:
		return
	t = l[x][y]
	f = 0
	for row in range(x, x + n):
		if f:
			break
		for col in range(y, y + n):
			if t != l[row][col]:
				f = 1
				break
	if f:
		m = n // 2
		r.append('(')
		recur(l, x, y, m, r), recur(l, x, y+m, m, r), recur(l, x+m, y, m, r), recur(l, x+m, y+m, m, r)
		r.append(')')
	else:
		r.append(t)

def solution():
	n = int(input())
	l = []
	r = []
	for _ in range(n):
		l.append(input().strip())
	recur(l, 0, 0, n, r)
	print(''.join(r))
	
if __name__ == "__main__":
	solution()
