import sys
input = sys.stdin.readline

def solution():
	n, c = map(int, input().split())
	l = []
	low, high = 1000000001, 0
	for _ in range(n):
		num = int(input())
		if num < low:
			low = num
		if num > high:
			high = num
		l.append(num)
	l.sort()
	left = 1
	right = (high - low) // (c - 1) + 1
	while left < right:
		mid = (right + left) // 2
		cnt = 1
		step = l[0] + mid
		for i in range(1, n):
			if l[i] >= step:
				cnt += 1
				step = l[i] + mid
		if cnt < c:
			right = mid
		else:
			left = mid + 1
	print(left - 1)


if __name__ == "__main__":
	solution()