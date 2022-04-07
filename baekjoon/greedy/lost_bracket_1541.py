import sys
input = sys.stdin.readline

def solution(lst):
	min_sum = sum(map(int, lst[0]))
	for l in lst[1:]:
		min_sum -= sum(map(int, l))
	return min_sum

if __name__ == "__main__":
	lst = list(map(lambda x:x.split('+'), input().strip().split('-')))
	print(solution(lst))