import sys
input = sys.stdin.readline

def solution():
	n, k = map(int, input().split())
	r = 1
	num = 1
	for i in range(1, n + 1):
		r *= i
		if i <= k:
			num *= i
		if i <= (n-k):
			num *= i
	print(int(r / num))

# ====================================================
# best time part_1
def solution2():
	n, k = map(int, input().split())
	mem = [[-1 for _ in range(k + 1)] for _ in range(n + 1)]
	
	def combine(n, k):
		if k == 0:
			return 1
		if k == n:
			return 1
		if mem[n][k] != -1:
			return mem[n][k]
		return combine(n - 1, k - 1) + combine(n - 1, k)

	print(mem)

# ====================================================
# best time part_2
def solution3():
	n, k = map(int, input().split())
	a = 1
	b = 1
	while k:
		a *= n
		b *= k
		n -= 1
		k -= 1
	print(int(a/b))

if __name__ == "__main__":
	solution()
	solution2()
	solution3()