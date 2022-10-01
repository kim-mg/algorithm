import sys
input = sys.stdin.readline

def solution():
	n = int(input())
	area = []
	for idx in range(6):
		i, l = map(int, input().split())
		if idx == 0:
			area.append(l)
		if idx > 0:
			area[-1] *= l
		if idx == 5:
			area[0] *= l
		else:
			area.append(l)
	print(n * (sum(area) - max(area) * 2))
			
if __name__ == "__main__":
	solution()