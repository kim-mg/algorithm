import sys
input = sys.stdin.readline

def to_ascii(x):
	if ord(x[0]) >= 97:
		return ord(x) - 97
	else:
		return int(x)

def solution(s, n, alpha, l):
	size = len(alpha)
	mem = [[0] * size]
	r = []
	for c in s:
		t = mem[-1].copy()
		if c in alpha:
			t[alpha[c]] += 1
		mem.append(t)
	for c, i, j in l:
		r.append(str(mem[j+1][alpha[c]] - mem[i][alpha[c]]))
	print('\n'.join(r))

if __name__ == "__main__":
	s = input().strip()
	n = int(input())
	l = []
	alpha = {}
	k = 0
	for _ in range(n):
		a, i, j = map(to_ascii, input().split())
		if chr(a + 97) not in alpha:
			alpha[chr(a + 97)] = k
			k += 1
		l.append([chr(a + 97), i, j])
	solution(s, n, alpha, l)