import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def get_ab(m):
	a, b = m + 1, m + 2
	if a > 2:
		a -= 3
	if b > 2:
		b -= 3
	return [a, b]

def solution(n, m, size):
	if n == size:
		a, b = get_ab(m)
		if n not in store:
			store[n] = [-1] * 3
		if store[n][m] == -1:
			store[n][m] = min(lst[n][a], lst[n][b])
		return store[n][m]
	a, b = get_ab(m)
	if n not in store:
		store[n] = [-1] * 3
	if store[n][m] == -1:
		store[n][m] = min(lst[n][a] + solution(n + 1, a, size), lst[n][b] + solution(n + 1, b, size))
	return store[n][m]

if __name__ == "__main__":
	n = int(input())
	lst = []
	store = {}
	for _ in range(n):
		l = list(map(int, input().split()))
		lst.append(l)
	print(solution(0, lst[0].index(max(lst[0])), n - 1))