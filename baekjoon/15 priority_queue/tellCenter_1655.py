import sys
input = sys.stdin.readline

###########################################################
# time out
def solution():
	n = int(input())
	max_h = [0]
	min_h = [0]
	a = []
	for _ in range(n):
		num = int(input())
		if max_h[0] <= min_h[0]:
			max_h.append(num)
			max_h[0] += 1
			c = max_h[0]
			p = c // 2
			while p > 0:
				if max_h[c] > max_h[p]:
					t = max_h[c]
					max_h[c] = max_h[p]
					max_h[p] = t
					c = p
					p = c // 2
				else:
					break
		else:
			min_h.append(num)
			min_h[0] += 1
			c = min_h[0]
			p = c // 2
			while p > 0:
				if min_h[c] < min_h[p]:
					t = min_h[c]
					min_h[c] = min_h[p]
					min_h[p] = t
					c = p
					p = c // 2
				else:
					break
		if min_h[0] == 0:
			a.append(str(max_h[1]))
		else:
			if min_h[1] >= max_h[1]:
				a.append(str(max_h[1]))
			else:
				t = min_h[1]
				min_h[1] = max_h[1]
				max_h[1] = t
				maxp = 1
				maxs = max_h[0] // 2
				while maxp <= maxs:
					ta = [maxp, maxp*2, min(max_h[0], maxp*2 + 1)]
					ta.sort(reverse=True, key=lambda x : max_h[x])
					maxc = ta[0]
					if maxp != maxc:
						tt = max_h[maxc]
						max_h[maxc] = max_h[maxp]
						max_h[maxp] = tt
						maxp = maxc
					else:
						break
				minp = 1
				mins = min_h[0] // 2
				while minp <= mins:
					ta = [minp, minp*2, min(min_h[0], minp*2 + 1)]
					ta.sort(key=lambda x : min_h[x])
					minc = ta[0]
					if minp != minc:
						tt = min_h[minc]
						min_h[minc] = min_h[minp]
						min_h[minp] = tt
						minp = minc
					else:
						break
				a.append(str(max_h[1]))
	print('\n'.join(a))

###############################################################
# use container
import heapq

def solution2():
	n = int(input())
	lq = []
	lq_size = 0
	sq = []
	sq_size = 0
	a = []
	for _ in range(n):
		num = int(input())
		if lq_size <= sq_size:
			heapq.heappush(lq, -num)
			lq_size += 1
		else:
			heapq.heappush(sq, num)
			sq_size += 1
		if sq_size == 0:
			a.append(str(-lq[0]))
		else:
			if sq[0] >= -lq[0]:
				a.append(str(-lq[0]))
			else:
				t = -lq[0]
				heapq.heapreplace(lq, -sq[0])
				heapq.heapreplace(sq, t)
				a.append(str(-lq[0]))
	print('\n'.join(a))

if __name__ == "__main__":
	# solution()
	solution2()