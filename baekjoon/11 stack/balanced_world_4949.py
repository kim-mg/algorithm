import sys
input = sys.stdin.readline

def solution(s):
	l = []
	cb = -1
	for c in s:
		if c == '(':
			cb = 0
			l.append(0)
		if c == '[':
			cb = 1
			l.append(1)
		if c == ')':
			if cb != 0:
				return "no"
			l.pop()
			cb = l[-1] if l else -1
		if c == ']':
			if cb != 1:	
				return "no"
			l.pop()
			cb = l[-1] if l else -1
	if l:
		return "no"
	return "yes"

if __name__ == "__main__":
	l = []
	while 1:
		l.append(input().rstrip())
		if len(l[-1]) == 1 and l[-1][0] == '.':
			l.pop()
			break

	for s in l:
		print(solution(s))

# =========================================================
# best time

def solution2(s):
	l = []
	for c in s:
		if c in '([':
			l.append(c)
		if c == ')':
			if not l or l.pop() != '(':
				return "no"
		if c == ']':
			if not l or l.pop() != '[':
				return "no"
	if l:
		return "no"
	return "yes"

if __name__ == "__main__":
	l = sys.stdin.readlines()
	l.pop()

	for s in l:
		print(solution2(s))
	