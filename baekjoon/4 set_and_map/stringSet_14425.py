import sys
input = sys.stdin.readline

def solution():
	n, m = map(int, input().split())
	s = set()
	ans = 0
	for _ in range(n):
		l = input().rstrip()
		s.add(l)
	for _ in range(m):
		l = input().rstrip()
		if l in s:
			ans += 1
	print(ans)


if __name__ == "__main__":
	solution()