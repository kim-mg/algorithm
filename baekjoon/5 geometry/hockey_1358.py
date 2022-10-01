import sys
input = sys.stdin.readline

def solution():
	w, h, x, y, p = map(int, input().split())
	ans = 0
	for _ in range(p):
		px, py = map(int, input().split())
		if px < x and (h/2)**2 >= (x-px)**2 + (y+h/2-py)**2:
			ans += 1
		if px > x+w and (h/2)**2 >= (x+w-px)**2 + (y+h/2-py)**2:
			ans += 1
		if x <= px <= x + w and y <= py <= y + h:
			ans += 1
	print(ans)

if __name__ == "__main__":
	solution()