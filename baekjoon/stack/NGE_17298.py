import sys
input = sys.stdin.readline

def solution(n, l):
	ans = ['-1'] * n
	stack = []
	for i in range(n):
		while stack and l[stack[-1]] < l[i]:
			ans[stack.pop()] = str(l[i])
		stack.append(i)
	return ' '.join(ans)

if __name__ == "__main__":
	n = int(input())
	l = list(map(int, input().split()))
	print(solution(n, l))
	