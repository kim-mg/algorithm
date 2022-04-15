import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def solution(n, m):
	# p = [i for i in range(n+1)]
	p = [-1] * (n + 1)
	ans = []

	def find(node):
		if p[node] < 0:
			return node
		p[node] = find(p[node])
		return p[node]

	def union(a, b):
		a = find(a)
		b = find(b)

		# if a < b:
		# 	p[b] = a
		# else:
		# 	p[a] = b
		if a != b:
			if p[a] < p[b]:
				p[a] += p[b]
				p[b] = a
			else:
				p[b] += p[a]
				p[a] = b

	for _ in range(m):
		flag, a, b = map(int, input().split())
		if flag:
			if find(a) == find(b):
				ans.append("YES")
			else:
				ans.append("NO")
		else:
			union(a, b)

	return '\n'.join(ans)

if __name__ == "__main__":
	n, m = map(int, input().split())
	print(solution(n, m))