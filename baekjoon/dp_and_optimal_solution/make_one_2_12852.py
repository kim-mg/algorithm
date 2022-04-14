import sys
input = sys.stdin.readline

def solution(n):
	g = [[0, []] for _ in range(n+1)]
	g[1][0] = 0
	g[1][1] = [1]

	for i in range(2, n+1):
		g[i][0] = g[i-1][0] + 1
		g[i][1] = g[i-1][1] + [i]

		if i % 3 == 0 and g[i//3][0] + 1 < g[i][0]:
			g[i][0] = g[i//3][0] + 1
			g[i][1] = g[i//3][1] + [i]
		
		if i % 2 == 0 and g[i//2][0] + 1 < g[i][0]:
			g[i][0] = g[i//2][0] + 1
			g[i][1] = g[i//2][1] + [i]

	print(g[n][0])
	print(' '.join(map(str, sorted(g[n][1], reverse=True))))

# ===============================================================
# best time
def solution2(n):
	mem = {1:0, 2:1}
	t = []

	def dp(n):
		if n in mem:
			return mem[n]
		mem[n] = 1 + min(dp(n//2) + n%2, dp(n//3) + n%3)
		return mem[n]

	def track(n):
		t.append(str(n))
		if n == 1:
			return
		if n == 2:
			t.append('1')
			return
		t_2 = mem[n//2] + n%2
		t_3 = mem[n//3] + n%3
		if t_2 < t_3:
			if n % 2 == 1:
				t.append(str(n - 1))
			track(n//2)
		else:
			for i in range(1, n%3 + 1):
				t.append(str(n - i))
			track(n//3)
	print(dp(n))
	track(n)
	print(' '.join(t))
	

if __name__ == "__main__":
	n = int(input())
	solution2(n)