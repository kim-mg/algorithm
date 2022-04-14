import sys
input = sys.stdin.readline

def solution(s):
	i = 0
	r = ''
	try:
		while s[i]:
			r += str(i)+'\n'
			i += 1
	except:
		print(r)

# =================================================
# best time
def solution2():
	print('\n'.join(map(str, range(len(input())))))

if __name__ == "__main__":
	s = input().strip()
	solution(s)