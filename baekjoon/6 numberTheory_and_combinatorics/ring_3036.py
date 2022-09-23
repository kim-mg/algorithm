import sys
input = sys.stdin.readline

def gcd(x, y):
	while y:
		x, y = y, x % y
	return x

def solution():
	n = int(input())
	l = list(map(int, input().split()))
	s = []
	x = l[0]
	for y in l[1:]:
		d = gcd(x, y)
		s.append(str(int(x/d)) + '/' + str(int(y/d)))
	print('\n'.join(s))

if __name__ == "__main__":
	solution()