import sys
from collections import deque
input = sys.stdin.readline

def solution():
	n = int(input())
	dq = [[0,'0'] for _ in range(n)]
	h = [0,0,0]
	line = ""

	def pf(num):
		if dq[h[0]][0] == 1:
			h[0] -= 1
			if h[0] < 0:
				h[0] = n - 1
		dq[h[0]][1] = num
		dq[h[0]][0] = 1
		h[2] += 1
		h[0] -= 1
		if h[0] < 0:
			h[0] = n - 1
	
	def pb(num):
		if dq[h[1]][0] == 1:
			h[1] += 1
			if h[1] > n - 1:
				h[1] = 0
		dq[h[1]][1] = num
		dq[h[1]][0] = 1
		h[2] += 1
		h[1] += 1
		if h[1] > n - 1:
			h[1] = 0

	def ppf():
		if h[2] == 0:
			return "-1"
		if dq[h[0]][0] == 0:
			h[0] += 1
			if h[0] > n - 1:
				h[0] = 0
		t = dq[h[0]][1]
		dq[h[0]][0] = 0
		h[2] -= 1
		return t
	
	def ppb():
		if h[2] == 0:
			return "-1"
		if dq[h[1]][0] == 0:
			h[1] -= 1
			if h[1] < 0:
				h[1] = n - 1
		t = dq[h[1]][1]
		dq[h[1]][0] = 0
		h[2] -= 1
		return t

	def size():
		return str(h[2])

	def empty():
		if h[2]:
			return "0"
		return "1"
	
	def front():
		if h[2] == 0:
			return "-1"
		t = h[0] + 1
		if t > n - 1:
			t = 0
		return dq[t][1]
	
	def back():
		if h[2] == 0:
			return "-1"
		t = h[1] - 1
		if h[1] < 0:
			h[1] = n - 1
		return dq[t][1]

	for _ in range(n):
		cm = input().split()
		if len(cm) > 1:
			if cm[0] == "push_front":
				pf(cm[1])
			if cm[0] == "push_back":
				pb(cm[1])
		elif cm[0] == "pop_front":
			line += ppf() + "\n"
		elif cm[0] == "pop_back":
			line += ppb() + "\n"
		elif cm[0] == "size":
			line += size() + "\n"
		elif cm[0] == "empty":
			line += empty() + "\n"
		elif cm[0] == "front":
			line += front() + "\n"
		elif cm[0] == "back":
			line += back() + "\n"
	print(line.rstrip("\n"))

def solution2():
	n = int(input())
	dq = deque()
	s = 0
	r = ""

	for _ in range(n):
		cm = input().split()
		if cm[0] == "push_front":
			dq.appendleft(cm[1])
			s += 1
		if cm[0] == "push_back":
			dq.append(cm[1])
			s += 1
		if cm[0] == "pop_front":
			if s == 0:
				r += "-1\n"
				continue
			r += dq.popleft() + "\n"
			s -= 1
		if cm[0] == "pop_back":
			if s == 0:
				r += "-1\n"
				continue
			r += dq.pop() + "\n"
			s -= 1
		if cm[0] == "size":
			r += str(s) + "\n"
		if cm[0] == "empty":
			if s:
				r += "0\n"
				continue
			r += "1\n"
		if cm[0] == "front":
			if s == 0:
				r += "-1\n"
				continue
			r += dq[0] + "\n"
		if cm[0] == "back":
			if s == 0:
				r += "-1\n"
				continue
			r += dq[s - 1] + "\n"
	print(r.rstrip('\n'))

if __name__ == "__main__":
	solution()
