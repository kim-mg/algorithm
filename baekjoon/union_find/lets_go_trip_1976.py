import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def solution(n, m):
	p = [i for i in range(n+1)]

	def find(node):
		if node == p[node]:
			return node
		p[node] = find(p[node])
		return p[node]

	def union(a, b):
		a = find(a)
		b = find(b)

		if a < b:
			p[b] = a
		else:
			p[a] = b

	for i in range(1, n+1):
		l = [0] + list(map(int, input().split()))
		for j in range(1, n+1):
			if l[j]:
				union(i, j)
	c = list(map(int, input().split()))
	s = p[c[0]]
	for i in range(1, m):
		if p[c[i]] != s:
			return "NO"
	return "YES"

# ===========================================================
# best time
def solution2(n, m):
	p = [-1] * n

	def find(node):
		if p[node] < 0:
			return node
		p[node] = find(p[node])
		return p[node]
	
	def union(a, b):
		a = find(a)
		b = find(b)

		if a == b:
			return None
		p[b] = a

	for i in range(n):
		l = list(map(int, input().split()))
		for j in range(i+1, n):
			if l[j]:
				union(i, j)
	print(p)
	c = list(map(int, input().split()))
	s = find(c[0]-1)
	for i in range(1, m):
		if find(c[i]-1) != s:
			return "NO"
	return "YES"


if __name__ == "__main__":
	n = int(input())
	m = int(input())
	print(solution2(n, m))