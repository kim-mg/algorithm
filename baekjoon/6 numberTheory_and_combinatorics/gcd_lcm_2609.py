import sys
input = sys.stdin.readline

# Euclidean algorithm
def gcd(x, y):
	while y:
		x, y = y, x % y
	return x

def lcm(x, y):
	return int(x * y / gcd(x, y))

def solution():
	n, m = map(int, input().split())
	print(gcd(n, m))
	print(lcm(n, m))

if __name__ == "__main__":
	solution()