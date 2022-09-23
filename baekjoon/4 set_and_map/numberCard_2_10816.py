import sys
input = sys.stdin.readline

def solution():
	n = int(input())
	s = input().rstrip().split()
	m = int(input())
	l = input().rstrip().split()
	d = {}
	for num in s:
		if num not in d:
			d[num] = 1
		else:
			d[num] += 1
	print(' '.join(str(d[x]) if x in d else "0" for x in l))

if __name__ == "__main__":
	solution()