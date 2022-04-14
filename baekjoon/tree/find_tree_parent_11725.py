import sys
input = sys.stdin.readline
sys.setrecursionlimit(2*(10**9))

def dfs(node):
	c[node] = 1
	for i in g[node]:
		if not c[i]:
			ans[i] = str(node)
			dfs(i)

def solution(n):
	for _ in range(n-1):
		a, b = map(int, input().split())
		g[a].append(b)
		g[b].append(a)
	dfs(1)
	return '\n'.join(ans[2:])

# ================================================================
# best time
# less than standard solve
def sol11725(n):
    parent = [0] * (n + 1)
    g = [[] for _ in range(n + 1)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)

    st = [1]
    visit = [False] * (n + 1)
    while st:
        node = st.pop()
        for c in g[node]:
            if not visit[c]:
                parent[c] = node
                st.append(c)
                visit[c] = True
    return '\n'.join(map(str, parent[2:]))

if __name__ == "__main__":
	n = int(input())
	g = [[] for _ in range(n+1)]
	c = [0 for _ in range(n+1)]
	ans = ['0'] * (n+1)
	print(solution(n))