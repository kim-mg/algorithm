import sys
input = sys.stdin.readline

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

def solution(n, k, p):
	r1 = 1
	r2 = 1
	
	for i in range(1, k+1):
		r1 = (r1 * (n - (i - 1))) % p
		r2 = (r2 * i) % p
	print(((r1 % p) * mod_square(r2, p-2, p)) % p)

# ============================================================
# best time
def euclidean(x, y):
	q = []
	while y:
		q.append(x // y)
		(x, y) = (y, x % y)
	q.pop()

	a, b = 0, 1
	for i in q[-1: :-1]:
		a, b = b, a - i*b
	print(q, a, b)
	return x, a, b

def solution2(n, k, p):
	k = min(k, n-k)
	if k == 0:
		return 1
	top = n
	bot = 1
	n += 1
	for i in range(2, k+1):
		top = top*(n-i)%p
		bot = bot*i%p
	g, inv, _ = euclidean(bot, p)
	return top*inv%p

if __name__ == "__main__":
	n, k = map(int, input().split())
	p = 1000000007
	solution(n, k, p)
	print(solution2(n, k, p))