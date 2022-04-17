import sys
input = sys.stdin.readline

def gcd(x, y):
	if x % y == 0:
		return y
	return gcd(y, x%y)

def get_divisors(x):
	l = []
	t = []
	for i in range(1, (x**2) + 1):
		if x % i == 0:
			l.append(i)
			t.append(x//i)
	print(l,t)

def solution(n, l):
	min_n = l[-1]
	max_n = 0
	for i in range(1, n+1):
		tmp = l[i] - l[i-1]
		if tmp < min_n:
			min_n = tmp
		if tmp > max_n:
			max_n = tmp
	cd = gcd(max_n, min_n)
	get_divisors(cd)
	pass

if __name__ == "__main__":
	n = int(input())
	l = []
	for _ in range(n):
		l.append(int(input()))
	l.sort()
	solution(n, l)
