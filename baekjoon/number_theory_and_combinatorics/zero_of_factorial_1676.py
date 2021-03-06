import sys
input = sys.stdin.readline

def count_ele(x, std):
	r = 0
	while x:
		t = x // std
		r += t
		x = t
	return r

def solution(n):
	print(min(count_ele(n, 2), count_ele(n, 5)))

# =====================================================
# best time
def solution2(n):
	print(n//5 + n//25 + n//125)

if __name__ == "__main__":
	n = int(input())
	solution(n)