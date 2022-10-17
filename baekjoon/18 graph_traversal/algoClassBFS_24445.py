import sys
from collections import deque
input = sys.stdin.readline

def solution():
	n, m, r = map(int, input().split())
	graph = [[] for _ in range(n+1)]
	visit = [0 for _ in range(n+1)]
	for _ in range(m):
		u, v = map(int, input().split())
		graph[u].append(v)
		graph[v].append(u)
	for i in range(1, n+1):
		graph[i].sort(reverse=True)
	q = deque([r])
	visit[r] = 1
	order = 2
	while q:
		u = q.popleft()
		for v in graph[u]:
			if not visit[v]:
				visit[v] = order
				order += 1
				q.append(v)
	print('\n'.join(map(str, visit[1:])))

if __name__ == "__main__":
	solution()