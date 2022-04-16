import sys
input = sys.stdin.readline

def solution(n, k):
	r = 1
	num = 1
	for i in range(1, n + 1):
		r *= i
		if i <= k:
			num *= i
		if i <= (n-k):
			num *= i
	print(int(r / num) % 10007)

# ====================================================
# best time part_1
def solution2(n, k):
	a = 1
	b = 1
	while k:
		a *= n
		b *= k
		n -= 1
		k -= 1
	print(int(int(a/b) % 10007))


if __name__ == "__main__":
	n, k = map(int, input().split())
	solution(n, k)
	solution2(n, k)