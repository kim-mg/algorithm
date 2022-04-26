import sys
from collections import deque
input = sys.stdin.readline

def solution():
	n = int(input())
	dq = ['0'] * n
	f = 0
	r = 0
	s = 0
	r = ""

	def pf(num):
		dq[f] = num
		f -= 1
		if f < 0:
			f = n - 1
	
	def pb(num):
		dq[r] = num
		r += 1

	def ppf():
		if s == 0:
			return "-1"
		t = dq[f + 1]
	for _ in range(n):
		cm = input().split()
		if len(cm) > 1:
			if cm[0] == "push_front":
				pf(cm[1])
			if cm[0] == "push_back":
				pb(cm[1])
			s += 1
		elif cm[0] == "pop_front":
			r += ppf() + "\n"
			s -= 1
	pass

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
	solution2()
