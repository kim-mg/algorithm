import sys
input = sys.stdin.readline

def solution(s, l, n):
	if n >= 1:
		s.append(l[0])
	if n >= 2:
		s.append(l[0] + l[1])
	if n >= 3:
		s.append(max(l[0] + l[2], l[1] + l[2], s[1]))
	for i in range(3, n):
		s.append(max(s[i-2] + l[i], s[i-3] + l[i] + l[i-1], s[i-1]))
	return s[n-1]

if __name__ == "__main__":
	n = int(input())
	lst = []
	sto = []
	
	for _ in range(n):
		lst.append(int(input()))

	print(solution(sto, lst, n))
