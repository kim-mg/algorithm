import sys
input = sys.stdin.readline

def solution():
	n = int(input())
	l1 = list(map(int, input().split()))
	m = int(input())
	l2 = list(map(int, input().split()))
	dp = {}
	r = []
	
	for i in l1:
		if i not in dp:
			dp[i] = 1
	
	for i in l2:
		if i in dp:
			r.append("1")
		else:
			r.append("0")
	
	print('\n'.join(r))

# ============================================================
# best time
def main():
    a = int(input())
    n = input().strip().split(' ')
    b = int(input())
    
    s = set(n)
    r = ''
    for k in input().strip().split(' '):
        r += '1\n' if k in s else '0\n'
    print(r)

if __name__ == "__main__":
	solution()
	main()
