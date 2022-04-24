import sys
from collections import deque
input = sys.stdin.readline

def solution(m, k, l, imp):
	deq = deque(l)
	im_deq = deque(imp)
	im = im_deq.popleft()
	p = 0
	while True:
		n = deq.popleft()
		if n[1] < im[1]:
			deq.append(n)
		else:
			p += 1
			if n[0] == k:
				break
			im = im_deq.popleft()
	
	print(p)

if __name__ == "__main__":
	n = int(input())
	for _ in range(n):
		m, k = map(int, input().split())
		l = [[i,n] for i, n in enumerate(map(int, input().split()))]
		imp = sorted(l, key=lambda x: x[1], reverse=True)
		solution(m, k, l, imp)
