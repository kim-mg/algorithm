import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def rec_sol(n, m, size):
	if n == size:
		return lst[n][m]
	if n not in store:
		store[n] = [-1] * (n + 1)
	if store[n][m] == -1:
		store[n][m] = max(lst[n][m] + rec_sol(n + 1, m, size), lst[n][m] + rec_sol(n + 1, m + 1, size))
	return store[n][m]

if __name__ == "__main__":
	n = int(input())
	lst = []
	store = {}
	for _ in range(n):
		l = list(map(int, input().split()))
		lst.append(l)
	print(rec_sol(0, 0, n - 1))

#######################################################################
# Faster solution

# def solution():
#     import sys
#     n = int(input())
#     triangle =[]
#     for _ in range(n):
#         triangle.append(list(map(int, sys.stdin.readline().rstrip().split())))
                   
#     accum = []
#     for i in range(n):
#         accum = [max(a+c, b+c) for a,b,c in zip([0]+accum, accum+[0], triangle[i])]
#     print(max(accum))
    

# solution()