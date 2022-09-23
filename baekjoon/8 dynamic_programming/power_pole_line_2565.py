import sys
input = sys.stdin.readline

def solution(p, n):
	lis = [1] * n
	p = sorted(p, key=lambda x:x[0])
	for i in range(n):
		for j in range(i):
			if p[i][1] > p[j][1]:
				lis[i] = max(lis[i], lis[j]+1)
	return n - max(lis)

if __name__ == "__main__":
	n = int(input())
	pole = []
	for _ in range(n):
		pole.append(list(map(int, input().split())))
	print(solution(pole,n))
