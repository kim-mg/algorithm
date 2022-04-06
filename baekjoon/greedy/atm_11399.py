import sys
input = sys.stdin.readline

def solution(lst, n):
	task = 0
	wait = 0
	lst = sorted(lst)
	for i in range(n):
		task += lst[i]
		wait += (n - i - 1) * lst[i]
	return task + wait

if __name__ == "__main__":
	n = int(input())
	lst = list(map(int, input().split()))
	print(solution(lst, n))
