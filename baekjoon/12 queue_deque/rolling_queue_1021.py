import sys
from collections import deque
input = sys.stdin.readline

def solution():
	n, m = map(int, input().split())
	t_l = list(map(int, input().split()))
	dq = deque([i for i in range(1, n+1)])
	r = 0

	for num in t_l:
		pull_cnt = dq.index(num)
		push_cnt = len(dq) - pull_cnt

		if pull_cnt < push_cnt:
			r += pull_cnt
			dq.rotate(-pull_cnt)
		else:
			r += push_cnt
			dq.rotate(push_cnt)
		
		dq.popleft()
	print(r)

if __name__ == "__main__":
	solution()
