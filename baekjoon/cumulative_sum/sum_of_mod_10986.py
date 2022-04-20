import sys
input = sys.stdin.readline

def solution(n, k):
	mod = [0] * k
	r = 0
	s = 0
	for i in map(int, input().split()):
		s += i
		m = s % k
		if m == 0:
			r += 1
		mod[m] += 1
	for i in range(k):
		r += mod[i] * (mod[i] - 1) // 2
	print(r)

if __name__ == "__main__":
	n, k = map(int, input().split())
	solution(n, k)