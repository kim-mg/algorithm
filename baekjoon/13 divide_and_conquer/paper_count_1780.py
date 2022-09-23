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
		m = n // 3
		mm = m * 2
		recur(l, x, y, m, r), recur(l, x, y+m, m, r), recur(l, x, y+mm, m, r)
		recur(l, x+m, y, m, r), recur(l, x+m, y+m, m, r), recur(l, x+m, y+mm, m, r)
		recur(l, x+mm, y, m, r), recur(l, x+mm, y+m, m, r), recur(l, x+mm, y+mm, m, r)
	else:
		r[t] += 1

def solution():
	n = int(input())
	l = []
	r = [0, 0, 0]
	for _ in range(n):
		l.append(list(map(int, input().split())))
	recur(l, 0, 0, n, r)
	print('\n'.join(map(str, r[2:] + r[:2])))
	
# ==============================================================
# best time
def nona(si, sj, ei, ej, n):
	global mat

	if n == 1:
		return mat[si][sj]

	tri = n // 3
	r1 = nona(si, sj, si + tri, sj + tri, tri)
	r2 = nona(si + tri, sj, si + 2 * tri, sj + tri, tri)
	r3 = nona(si + 2 * tri, sj, ei, sj + tri, tri)
	r4 = nona(si, sj + tri, si + tri, sj + 2 * tri, tri)
	r5 = nona(si + tri, sj + tri, si + 2 * tri, sj + 2 * tri, tri)
	r6 = nona(si + 2 * tri, sj + tri, ei, sj + 2 * tri, tri)
	r7 = nona(si, sj + 2 * tri, si + tri, ej, tri)
	r8 = nona(si + tri, sj + 2 * tri, si + 2 * tri, ej, tri)
	r9 = nona(si + 2 * tri, sj + 2 * tri, ei, ej, tri)

	if r1 == r2 == r3 == r4 == r5 == r6 == r7 == r8 == r9 and len(r1) == 1:
		return r1
	return r1 + r2 + r3 + r4 + r5 + r6 + r7 + r8 + r9

def solution2():
	N = int(input())
	mat = [input().replace('-1', '2').split() for _ in range(N)]
	papers = nona(0, 0, 0, 0, N)
	for p in [papers.count(n) for n in ['2', '0', '1']]:
		print(p)

if __name__ == "__main__":
	solution()
	solution2()
