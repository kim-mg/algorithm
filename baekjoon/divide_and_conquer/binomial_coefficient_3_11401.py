import sys
input = sys.stdin.readline

p = 1000000007

def facto(n):
	r = 1
	for i in range(2, n+1):
		r = (r * i) % p
	return r

def mod_square(n, k, p):
	if k == 1:
		return n
	
	mod = mod_square(n, k//2, p)
	if k % 2:
		return (mod * mod * n) % p
	else:
		return (mod * mod) % p

def solution(n, k):
	r1 = 1
	r2 = 1
	
	for i in range(1, k+1):
		r1 = (r1 * (n - (i - 1))) % p
		r2 = (r2 * i) % p
	print(((r1 % p) * mod_square(r2, p-2, p)) % p)

if __name__ == "__main__":
	n, k = map(int, input().split())
	solution(n, k)