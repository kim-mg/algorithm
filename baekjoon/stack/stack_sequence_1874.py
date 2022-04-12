import sys
input = sys.stdin.readline

def solution(n, comp):
	stack = []
	s = ""
	idx = 0
	for i in range(1, n+1):
		stack.append(i)
		s += "+\n"
		while stack and stack[-1] == comp[idx]:
			stack.pop()
			s += "-\n"
			idx += 1
			
	if stack:
		s = "NO"
	return s

# ==========================================================
# best time
# more simple logic
input2 = sys.stdin.read

def sol1874():
    n, *nums = map(int, input2().split())
    cur = 1
    st = []
    answer = []
    for num in nums:
        while cur <= num:
            st.append(cur)
            answer.append('+')
            cur += 1
        if st[-1] != num:
            answer = ['NO']
            break
        st.pop()
        answer.append('-')
    print('\n'.join(answer))

if __name__ == "__main__":
	n = int(input())
	ans = []
	for _ in range(n):
		ans.append(int(input()))
	print(solution(n, ans))
	# sol1874()
	