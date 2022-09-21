import sys
input = sys.stdin.readline

def recursion(s, l, r):
	if l >= r: return "1 " + str(l+1)
	elif s[l] != s[r]: return "0 " + str(l+1)
	else: return recursion(s, l+1, r-1)

def isPalindrome(s):
	return recursion(s, 0, len(s) - 1)

def solution():
	n = int(input())
	for _ in range(n):
		s = input().rstrip()
		print(isPalindrome(s))

#################################################################
# best time
import sys
input = sys.stdin.readline

def best():
	n = int(input())
	ans = []
	for _ in range(n):
		s = input().strip()
		if s == s[::-1]:
			ans.append(f'1 {len(s)//2 + 1}')
			continue
		for i in range((len(s)+1)//2):
			if s[i] != s[-i-1]:
				ans.append(f'0 {i+1}')
				break
	print('\n'.join(ans))

if __name__ == "__main__":
	# solution()
	best()