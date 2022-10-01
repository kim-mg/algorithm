import sys
input = sys.stdin.readline
f2 = 0

def fibonacci(n, g):
	global f2
	if n in g:
		return g[n]
	f2 += 1
	g[n] = fibonacci(n-1, g) + fibonacci(n-2, g)
	return g[n]

def solution():
	g = {0:0, 1:1, 2:1}
	n = int(input())
	print(fibonacci(n, g), f2)

if __name__ == "__main__":
	solution()