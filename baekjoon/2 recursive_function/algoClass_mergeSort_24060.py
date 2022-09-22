import sys
input = sys.stdin.readline

def merge(a, p, q, r, ans):
	i = p
	j = q + 1
	tmp = []
	while i <= q and j <= r:
		if a[i] <= a[j]:
			tmp.append(a[i])
			i += 1
		else:
			tmp.append(a[j])
			j += 1
	while i <= q:
		tmp.append(a[i])
		i += 1
	while j <= r:
		tmp.append(a[j])
		j += 1
	i = p
	t = 0
	# print(a, p, q, r, tmp)
	while i <= r:
		a[i] = tmp[t]
		ans[0] += 1
		if (ans[0] == ans[1]):
			ans.append(a[i])
		i += 1
		t += 1

def merge_sort(a, p, r, ans):
	if p < r:
		q = (p + r) // 2
		merge_sort(a, p, q, ans)
		merge_sort(a, q+1, r, ans)
		merge(a, p, q, r, ans)

def solution():
	l, k = map(int, input().split())
	a = list(map(int, input().split()))
	ans = [0, k]
	merge_sort(a, 0, l - 1, ans)
	if (ans[0] < ans[1]):
		ans.append(-1)
	print(ans[-1])

#####################################################################
# best
# merge 시점마다 횟수를 계산할 수 있다.
# 횟수를 계산하고 비교해 결과를 도출한다.
import sys
input = sys.stdin.readline

def sol(n, k, a):

	def sol_rec(beg, l):
		if l <= 1:
			return None
		half = (l + 1) // 2
		if (ret := sol_rec(beg, half)) is not None:
			return ret
		if (ret := sol_rec(beg + half, l - half)) is not None:
			return ret
		nonlocal k
		if k <= l:
			return sorted(a[beg:beg + l])[k - 1]
		else:
			k -= l
			return None

	return sol_rec(0, n)

def best():
	n, k = map(int, input().split())
	a = list(map(int, input().split()))

	answer = sol(n, k, a)
	print('-1' if answer is None else answer)

if __name__ == "__main__":
	# solution()
	best()