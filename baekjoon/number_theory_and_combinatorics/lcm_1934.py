import sys
input = sys.stdin.readline

def gcd(x, y):
	while y:
		x, y = y, x % y
	return x

def lcm(x, y):
	return int(x * y / gcd(x, y))

def solution():
	n = int(input())
	s = []
	for _ in range(n):
		x, y = map(int, input().split())
		s.append(str(lcm(x, y)))
	print('\n'.join(s))

if __name__ == "__main__":
	solution()