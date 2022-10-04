import sys
input = sys.stdin.readline

def solution(s1, s2):
	n = len(s1)
	m = len(s2)
	dp = [[0] * (m+1) for _ in range(n+1)]

	for i in range(1, n+1):
		for j in range(i, m+1):
			if s1[i-1] == s2[j-1]:
				dp[i][j] = dp[i-1][j-1] + 1
			else:
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])
	print(dp)
	return dp[n][m]

# ====================================================
# best time
def solution2(s1, s2):
	d=[0]*300;r=0;z=0;c=0
	for i in range(len(s1)):d[ord(s1[i])]+=(2**i)
	for i in range(len(s1)):
		if(s1[i]==s2[0]):r+=(2**i);break
	for i in range(1,len(s2)):
		z=d[ord(s2[i])]|r
		r=z&(z^(z-(r*2+1)))
	while(r):c+=(r%2);r//=2
	return c

if __name__ == "__main__":
	s1 = input().strip()
	s2 = input().strip()
	print(solution(s1, s2))