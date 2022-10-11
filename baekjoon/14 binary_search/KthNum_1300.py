import sys
input = sys.stdin.readline

def solution():
	n = int(input())
	k = int(input())

	left = 1
	right = k
	while left < right:
		mid = (right + left) // 2
		cnt = 0
		for i in range(1, n + 1):
			cnt += min(n, mid // i)
			if cnt > k:
				break
		if cnt >= k:
			right = mid
		else:
			left = mid + 1
	print(left)


if __name__ == "__main__":
	solution()