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
		return recur(l, x, y, m, r), recur(l, x, y+m, m, r), recur(l, x+m, y, m, r), recur(l, x+m, y+m, m, r)
	else:
		r[t] += 1

def solution():
	n = int(input())
	l = []
	r = [0,0]
	for _ in range(n):
		t = list(map(int, input().split()))
		l.append(t)
	recur(l, 0, 0, n, r)
	print(r[0])
	print(r[1])
	
if __name__ == "__main__":
	solution()
