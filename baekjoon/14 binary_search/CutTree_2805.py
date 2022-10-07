import sys
input = sys.stdin.readline

def solution():
	n, m = map(int, input().split())
	l = list(map(int, input().split()))
	
	left = (sum(l) // n) - m
	right = max(l) + 1
	while left < right:
		mid = (right + left) // 2
		t = 0
		for i in range(n):
			if l[i] > mid:
				t += l[i] - mid
			if t > m:
				break
		if t < m:
			right = mid
		else:
			left = mid + 1
	print(left - 1)

#############################################################
# effecient
from collections import Counter
def solution2():
	n, m = map(int, input().split())
	l = Counter(map(int, input().split()))

	left = (sum([wood * n for wood, n in l.items()]) - m) // n
	right = max(l) + 1
	while left < right:
		mid = (right + left) // 2
		t = 0
		for wood, n in l.items():
			if wood > mid:
				t += (wood - mid) * n
			if t > m:
				break
		if t < m:
			right = mid
		else:
			left = mid + 1
	print(left - 1)

# 4 7
# 20 15 10 17

if __name__ == "__main__":
	# solution()
	solution2()