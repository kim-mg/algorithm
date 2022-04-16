import sys
input = sys.stdin.readline

def solution():
	n = int(input())
	l = list(map(int, input().split()))
	print(min(l) * max(l))

if __name__ == "__main__":
	solution()