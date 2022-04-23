import sys
input = sys.stdin.readline

def solution(n, k):
	l = [str(i) for i in range(1, n+1)]
	r = "<"
	i = k - 1
	
	while n > 1:
		r += l.pop(i) + ", "
		i += k - 1
		n -= 1
		i %= n
	print(r + l.pop(i) + ">")

if __name__ == "__main__":
	n, k = map(int, input().split())
	solution(n, k)