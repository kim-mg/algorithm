import sys
input = sys.stdin.readline

def solution(l, n):
	for i in range(1, n):
		l.append([0] *10)
		for j in range(10):
			if j == 0:
				l[i][j] = l[i-1][j+1]
			if j == 9:
				l[i][j] = l[i-1][j-1]
			if 0 < j < 9:
				l[i][j] = l[i-1][j-1] + l[i-1][j+1]
	return sum(l[-1])

if __name__ == "__main__":
	n = int(input())
	sto = [[0] + [1] * 9]
	print(int(solution(sto, n) % 1000000000))
