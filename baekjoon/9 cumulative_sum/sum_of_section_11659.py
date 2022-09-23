import sys
input = sys.stdin.readline

def solution(n, k, l):
	r = []
	for i in range(1, n+1):
		l[i] += l[i-1]
	for _ in range(k):
		n, m = map(int, input().split())
		r.append(str(l[m] - l[n-1]))
	print('\n'.join(r))

if __name__ == "__main__":
	n, k = map(int, input().split())
	l = [0] + list(map(int, input().split()))
	solution(n, k, l)