import sys
input = sys.stdin.readline

def solution():
	n, m = map(int, input().split())
	d = {}
	for i in range(1, n + 1):
		p = input().rstrip()
		d[p] = str(i)
		d[str(i)] = p
	print('\n'.join(d[input().rstrip()] for _ in range(m)))

if __name__ == "__main__":
	solution()