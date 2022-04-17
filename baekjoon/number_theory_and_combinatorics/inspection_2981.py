import sys
input = sys.stdin.readline

def gcd(x, y):
	if x % y == 0:
		return y
	return gcd(y, x%y)

def get_divisors(x):
	l = []
	t = []
	for i in range(1, int((x**(1/2))) + 1):
		if x % i == 0:
			l.append(i)
			t.append(x//i)
	t.sort()
	if l[-1] == t[0]:
		return l + t[1:]
	return l + t

def solution(n, l):
	sub = []
	for i in range(1, n):
		sub.append(l[i] - l[i-1])
	mcd = sub[0]
	for i in range(1, n-1):
		mcd = gcd(mcd, sub[i])
	r2 = map(str, get_divisors(mcd)[1:])
	print(' '.join(r2))
	

if __name__ == "__main__":
	n = int(input())
	l = []
	for _ in range(n):
		l.append(int(input()))
	l.sort()
	solution(n, l)