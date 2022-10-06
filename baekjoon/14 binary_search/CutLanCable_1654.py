import sys
input = sys.stdin.readline

def solution():
	n, m = map(int, input().split())
	l = []
	std = 0
	for _ in range(n):
		lan = int(input())
		std += lan / m
		l.append(lan)

	left = 0
	right = int(std) + n
	while left < right:
		mid = (right + left) // 2
		t = 0
		for i in range(n):
			t += l[i] // mid
		if t < m:
			right = mid
		else:
			left = mid + 1
	print(int(left) - 1)

# 4 11
# 802
# 743
# 457
# 539

if __name__ == "__main__":
	solution()