import sys
input = sys.stdin.readline

def solution():
	def divConquer(left, right):
		nonlocal l
		if left == right: return l[left]
		mid = left + ((right - left) // 2)
		ans = max(divConquer(left, mid), divConquer(mid + 1, right))

		pos_l = mid
		pos_r = mid + 1
		min_h = 1000000000 + 1
		while left <= pos_l and pos_r <= right:
			min_h = min(min_h, l[pos_l], l[pos_r])
			ans = max(ans, (pos_r - pos_l + 1) * min_h)
			if pos_l == left: pos_r += 1
			elif pos_r == right: pos_l -= 1
			elif l[pos_l - 1] <= l[pos_r + 1]: pos_r += 1
			else: pos_l -= 1
		return ans
	
	a = []
	while True:
		l = list(map(int, input().split()))
		n = l[0]
		if n == 0:
			break
		l = l[1:]
		a.append(str(divConquer(0, len(l) - 1)))
	print('\n'.join(a))

from collections import deque

def solution2():
	a = []
	while True:
		l = list(map(int, input().split()))
		n = l[0]
		if n == 0:
			break
		l = l[1:] + [-1]
		s = deque([-1])
		ans = 0
		for i in range(n + 1):
			while len(s) > 1 and l[i] < l[s[-1]]:
				height = s.pop()
				left = s[-1]
				ans = max(ans, (i - left - 1) * l[height])
			s.append(i)
		a.append(str(ans))
	print('\n'.join(a))

# 7 2 1 4 5 1 3 3
# 4 1000 1000 1000 1000
# 0

if __name__ == "__main__":
	# solution()
	solution2()