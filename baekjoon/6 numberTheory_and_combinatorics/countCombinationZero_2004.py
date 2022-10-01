import sys
input = sys.stdin.readline

def count_num(n, std):
	c = 0
	while n > 0:
		n = n // std
		c += n
	return c

def solution(n, m):
	c2 = count_num(n, 2) - count_num(m, 2) - count_num(n-m, 2)
	c5 = count_num(n, 5) - count_num(m, 5) - count_num(n-m, 5)
	return min(c2, c5)

if __name__ == "__main__":
	n, m = map(int, input().split())
	print(solution(n, m))