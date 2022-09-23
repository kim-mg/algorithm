import sys
input = sys.stdin.readline

def solution():
	n, m = map(int, input().split())
	# vscode 실행방법 못찾음
	# pr = sys.stdin.read().rstrip().split('\n')
	l = set()
	s = set()
	for _ in range(n):
		name = input().rstrip()
		l.add(name)
	for _ in range(m):
		name = input().rstrip()
		s.add(name)
	c = sorted(l & s)
	print(str(len(c)), '\n'.join(c), sep='\n')

if __name__ == "__main__":
	solution()