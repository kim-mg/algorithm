import sys
input = sys.stdin.readline

def solution(lst, n):
	dp = [lst[0]]  + [0] * (n-1)
	for i in range(1, n):
		dp[i] = max(lst[i], dp[i-1] + lst[i])
	return max(dp)

def solution2(lst, n):
	tmp = lst[0]
	m = tmp
	for i in range(1, n):
		if tmp > 0 and tmp + lst[i] > 0:
			tmp += lst[i]
		else:
			tmp = lst[i]
		if m < tmp:
			m = tmp
	return m

if __name__ == "__main__":
	n = int(input())
	lst = list(map(int, input().split()))
	print(solution2(lst, n))