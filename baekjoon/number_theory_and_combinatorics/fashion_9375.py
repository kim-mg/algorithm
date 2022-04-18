import sys
input = sys.stdin.readline

def solution(n):
	dic = {}
	kind = []
	r = 1

	for _ in range(n):
		c, k = input().strip().split()
		if k not in dic:
			dic[k] = 0
			kind.append(k)
		dic[k] += 1
	for k in kind:
		r *= (dic[k] + 1)
	print(r-1)

if __name__ == "__main__":
	n = int(input())
	for _ in range(n):
		m = int(input())
		solution(m)