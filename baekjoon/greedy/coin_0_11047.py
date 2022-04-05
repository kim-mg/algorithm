import sys
input = sys.stdin.readline

def solution(lst, n, cost):
	cnt = 0
	for coin in lst:
		if cost // coin:
			cnt += (int)(cost / coin)
			cost = cost % coin
	return cnt

if __name__ == "__main__":
	n = list(map(int, input().split()))
	lst = []
	for _ in range(n[0]):
		lst.append(int(input()))
	lst.reverse()
	print(solution(lst, n[0], n[1]))
