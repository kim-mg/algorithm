import sys
input = sys.stdin.readline

def solution():
	n = int(input())
	a = set(input().split())
	m = int(input())
	b = input().split()
	ans = []
	for comp in b:
		if comp in a:
			ans.append("1")
		else:
			ans.append("0")
	# more faster use generator object class
	# print(' '.join("1" if x in a else "0" for x in b))
	print(' '.join(ans))

if __name__ == "__main__":
	solution()