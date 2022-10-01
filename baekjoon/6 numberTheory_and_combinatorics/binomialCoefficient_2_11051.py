import sys
input = sys.stdin.readline

# failed

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
	sto = [[1 for _ in range(k+1)] for _ in range(n+1)]
	print(sto)
	for i in range(1, k+1):
		for j in range(i+1, n+1):
			sto[j][i] = (sto[j-1][i-1] + sto[j-1][i]) % 10007
	print(sto)
	print(sto[n][k])

# ====================================================
# best time part_2
def solution3(n, k):
	r = 1
	for i in range(k):
		r *= n-i
		r //= i+1
	print(r%10007)

if __name__ == "__main__":
	n, k = map(int, input().split())
	solution(n, k)
	solution2(n, k)
	solution3(n, k)