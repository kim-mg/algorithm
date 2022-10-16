import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def solution():
	def dfs(r):
		nonlocal p
		nonlocal seq
		nonlocal visited
		nonlocal graph

		seq += 1
		p[r] = seq
		visited[r] = 1
		for i in graph[r]:
			if visited[i] == 0:
				dfs(i)
	
	n, m, r = map(int, input().split())
	visited = [0 for _ in range(n)]
	p = [0 for _ in range(n)]
	graph = [[] for _ in range(n)]
	seq = 0
	for _ in range(m):
		u, v = map(lambda x : int(x) - 1, input().split())
		graph[u].append(v)
		graph[v].append(u)
	for i in range(n):
		graph[i].sort()
	dfs(r - 1)
	print('\n'.join(map(str, p)))

def solution2():
	n, m, r = map(int, input().split())
	graph = [[] for _ in range(n + 1)]
	visit = [0 for _ in range(n + 1)]
	for _ in range(m):
		u, v = map(int, input().split())
		graph[u].append(v)
		graph[v].append(u)
	for g in graph[1:]:
		g.sort(reverse=True)

	order = 1
	stack = [r]
	while stack:
		pv = stack.pop()
		if visit[pv]:
			continue
		visit[pv] = order
		order += 1

		for cv in graph[pv]:
			if not visit[cv]:
				stack.append(cv)
	print('\n'.join(map(str, visit[1:])))
		

if __name__ == "__main__":
	# solution()
	solution2()