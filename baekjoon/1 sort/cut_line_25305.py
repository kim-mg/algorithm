import sys
input = sys.stdin.readline

def solution():
	n, k = map(int, input().split())
	l = list(map(int, input().split()))
	l.sort(reverse=True)
	print(l[k-1])


if __name__ == "__main__":
	solution()