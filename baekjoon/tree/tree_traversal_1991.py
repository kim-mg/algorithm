import sys
input = sys.stdin.readline

def traversal(node, order, g, ans):
	# preorder
	if order == 0:
		ans.append(node)
		if g[node][0] != '.':
			traversal(g[node][0], 0, g, ans)
		if g[node][1] != '.':
			traversal(g[node][1], 0, g, ans)
	# inorder
	if order == 1:
		if g[node][0] != '.':
			traversal(g[node][0], 1, g, ans)
		ans.append(node)
		if g[node][1] != '.':
			traversal(g[node][1], 1, g, ans)
	# postorder
	if order == 2:
		if g[node][0] != '.':
			traversal(g[node][0], 2, g, ans)
		if g[node][1] != '.':
			traversal(g[node][1], 2, g, ans)
		ans.append(node)

def solution(n):
	g = {}
	ans = []
	s = ''
	for _ in range(n):
		p, l, r = input().split()
		g[p] = [l, r]
	traversal('A', 0, g, ans)
	s = ''.join(ans)
	ans = []
	traversal('A', 1, g, ans)
	s = s + '\n' + ''.join(ans)
	ans = []
	traversal('A', 2, g, ans)
	s = s + '\n' + ''.join(ans)
	return s

if __name__ == "__main__":
	n = int(input())
	print(solution(n))