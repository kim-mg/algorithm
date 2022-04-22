import sys
input = sys.stdin.readline

def solution(n):
	s = 2
	
	if n == 1 or n == 2:
		print(n)
		return
	while s < n:
		s *= 2
	s //= 2
	print((n - s) * 2)

if __name__ == "__main__":
	n = int(input())
	solution(n)