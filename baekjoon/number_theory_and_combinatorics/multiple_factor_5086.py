import sys
input = sys.stdin.readline

def solution(n, m):
	if m % n == 0:
		return "factor"
	if n % m == 0:
		return "multiple"
	return "neither"

if __name__ == "__main__":
	while 1:
		n, m = map(int, input().split())
		if not n and not m:
			break
		print(solution(n, m))
	