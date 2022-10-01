import sys
input = sys.stdin.readline

def solution():
	case = int(input())
	ans = [0 for _ in range(case)]
	for i in range(case):
		sx, sy, ex, ey = map(int, input().split())
		galaxy = int(input())
		for _ in range(galaxy):
			gx, gy, gr = map(int, input().split())
			r = gr**2
			dist_s = (gx-sx)**2 + (gy-sy)**2
			dist_e = (gx-ex)**2 + (gy-ey)**2
			if ((dist_s > r and dist_e < r) or (dist_s < r and dist_e > r)):
				ans[i] += 1
	print('\n'.join(map(str, ans)))

if __name__ == "__main__":
	solution()