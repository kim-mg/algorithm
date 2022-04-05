import sys
input = sys.stdin.readline

def solution(lst, n):
	cnt = 0
	end = 0
	for t in lst:
		if t[0] >= end:
			end = t[1]
			cnt += 1
	return cnt

if __name__ == "__main__":
	n = int(input())
	lst = []
	for _ in range(n):
		lst.append(list(map(int, input().split())))
	lst = sorted(lst, key=lambda x:(x[1], x[0]))
	print(solution(lst, n))
