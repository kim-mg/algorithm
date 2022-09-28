import sys
input = sys.stdin.readline

def solution():
	string = input().rstrip()
	s = set()
	for i in range(1, len(string) + 1):
		l = 0
		while l + i <= len(string):
			s.add(string[l:l+i])
			l += 1
	print(len(s))

###################################################################3
# best
import sys
input = sys.stdin.readline

def getsfxarr(s):
	n = len(s)
	t = 1
	sfxarr = list(range(n))
	group = [ord(s[i]) for i in range(n)] + [-1]
	newgroup = [0 for _ in range(n + 1)]
	newgroup[sfxarr[0]] = 0
	newgroup[n] = -1
	while t < n:
		# suffix 첫 글자를 기준으로 그룹을 나눈다.
		# 멘버-마이어스 알고리즘의 비교함수가 있지만, 풀어서 사용한 파이썬의 문법이다.
		sfxarr.sort(key = lambda x: (group[x], group[min(x+t, n)]))
		print(sfxarr, group, newgroup, t)
		# 나눠진 suffix를 토대로 그룹 내의 다음 문자열에 대한 비교를 시행
		for i in range(1, n):
			p, q = sfxarr[i-1], sfxarr[i]
			if group[p] != group[q] or group[min(p + t, n)] != group[min(q + t, n)]:
				newgroup[q] = newgroup[p] + 1
			else:
				newgroup[q] = newgroup[p]
			print(i, newgroup, p, q)
		group = newgroup[:]
		# t에 2를 곱한다(여기서는 시프트 연산)
		# t를 2의 지수승으로 갖는 이유는 글자 순서에 따른 그룹이 이미 정렬된 상태기 때문에
		# 두 글자씩 정렬된 그룹에서의 비교는 곧 4글자의 검증과 같기 때문이다.
		t <<= 1
	return sfxarr

def getlcp(s):
	n = len(s)
	sfxarr = getsfxarr(s)
	k = 0
	lcp = [0 for _ in range(n)]
	inv_sfxarr = [0 for _ in range(n)]
	# s 에 대해 sfxarr 에서의 순서를 입력한다.
	for i in range(n):
		inv_sfxarr[sfxarr[i]] = i
	# s 의 i 순의 접미사 a 로부터 sfxarr 에서 a-1 접미사와의 lcp를 구하면
	# s 의 i+1 순의 접미사 b 는 최소 lcp(a-1, a) - 1 <= lcp(b-1, b)가 된다.
	for i in range(n):
		if inv_sfxarr[i]:
			# inv_arr 에 저장해둔 sfxarr의 순서로 본인 앞 접미사를 구해와 비교할 수 있다.
			j = sfxarr[inv_sfxarr[i] - 1]
			# 같은 글자 수 k 만큼 lcp 값을 구하고 lcp 배열에 입력한다.
			while (j + k < n and i + k < n) and s[j + k] == s[i + k]:
				k += 1
			lcp[inv_sfxarr[i]] = k
			# print(s, i, j, k, inv_sfxarr, inv_sfxarr[i], sfxarr, sfxarr[j])
			# s 의 i+1 접미사의 최소 lcp 이므로 -1을 연산한다.
			if k > 0:
				k -= 1
	# print(lcp, sfxarr, inv_sfxarr)
	return lcp

def best():
	s = input().rstrip()
	n = len(s)
	print(n*(n+1)//2 - sum(getlcp(s)))

if __name__ == "__main__":
	# solution()
	best()