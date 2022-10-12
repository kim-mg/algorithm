import sys
input = sys.stdin.readline

def solution():
	n = int(input())
	l = [0]
	a = []
	for _ in range(n):
		num = int(input())
		if num == 0:
			if l[0] == 0:
				a.append('0')
			else:
				t = l[1]
				l[1] = l[-1]
				l[-1] = t
				a.append(str(l.pop()))
				l[0] -= 1
				p = 1
				pp = l[0] // 2
				while p <= pp:
					ta = [p, p*2, min(l[0], p*2 + 1)]
					ta.sort(key=lambda x : l[x])
					c = ta[0]
					if c != p:
						t = l[c]
						l[c] = l[p]
						l[p] = t
						p =  c
					else:
						break
		else:
			l.append(num)
			l[0] += 1
			c = l[0]
			p = c // 2
			while p > 0 and l[c] < l[p]:
				t = l[c]
				l[c] = l[p]
				l[p] = t
				c = p
				p //= 2
	print('\n'.join(a))

###############################################################
# use container
import heapq

def solution2():
	n = int(input())
	q = []
	a = []
	for _ in range(n):
		num = int(input())
		if num:
			heapq.heappush(q, num)
		else:
			a.append(str(heapq.heappop(q)) if q else '0')
	print('\n'.join(a))

if __name__ == "__main__":
	solution()
	# solution2()