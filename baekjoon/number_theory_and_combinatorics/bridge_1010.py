import sys
input = sys.stdin.readline

def comb_nr(r, n):
	tmp = 1
	for i in range(r):
		tmp *= (n - i)
		tmp //= (i + 1)
	return tmp

def solution(n, l):
	s = []
	for case in l:
		s.append(str(comb_nr(case[0], case[1])))
	print('\n'.join(s))

if __name__ == "__main__":
	n = int(input())
	l = []
	for _ in range(n):
		l.append(list(map(int, input().split())))
	solution(n, l)