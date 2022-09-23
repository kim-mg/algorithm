import sys
input = sys.stdin.readline

def solution():
	n, m = map(int, input().split())
	a = set(input().rstrip().split())
	b = set(input().rstrip().split())
	print(len(a-b) + len(b-a))

if __name__ == "__main__":
	solution()