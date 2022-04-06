import sys
input = sys.stdin.readline

def solution(n, d, c):
	cost = 0
	cur_city = c[0]
	for i in range(n-1):
		if cur_city > c[i]:
			cur_city = c[i]
		cost += d[i] * cur_city
	return cost

if __name__ == "__main__":
	n = int(input())
	distance = list(map(int, input().split()))
	city = list(map(int, input().split()))
	print(solution(n, distance, city))
