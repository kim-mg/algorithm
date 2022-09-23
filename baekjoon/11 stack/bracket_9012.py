import sys
input = sys.stdin.readline

def solution(s):
	v = 0
	if s[0] == ')':
		return "NO"
	for c in s:
		if c == ')':
			v -= 1
		else:
			v += 1
		if v < 0:
			return "NO"
	if v:
		return "NO"
	return "YES"

if __name__ == "__main__":
	n = int(input())
	l = []
	for _ in range(n):
		l.append(input().strip())

	for s in l:
		print(solution(s))
	