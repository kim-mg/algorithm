import sys
input = sys.stdin.readline

def solution(l, n, w):
	dp = [[0] * (w+1) for _ in range(n+1)]
	i = 0
	for weight, value in l:
		i += 1
		for j in range(1, w+1):
			dp[i][j] = dp[i-1][j]
			if j >= weight and dp[i][j] < value + dp[i-1][j-weight]:
				dp[i][j] = value + dp[i-1][j-weight]
	return dp[n][w]

# ========================================================
# best time

def solution2(l, n, k):
	kk = k+1
	bag = {}
	bag[0]=0
	l.sort(reverse=True)
	for w, v in l:
		tmp = {}
		print(w, v)
		for vv, ww in bag.items():
			if bag.get(vvv:=vv+v,kk) > (www:=w+ww):
				tmp[vvv]=www
			print(vv, ww, tmp)
		bag.update(tmp)
	return max(bag.keys())

if __name__ == "__main__":
	n, w = map(int, input().split())
	lst = []
	for _ in range(n):
		lst.append(list(map(int, input().split())))
	print(solution2(lst, n, w))