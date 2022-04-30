import sys
input = sys.stdin.readline

# https://velog.io/@gidskql6671/%EB%82%98%EB%A8%B8%EC%A7%80Modulo-%EC%97%B0%EC%82%B0-%EB%B6%84%EB%B0%B0%EB%B2%95%EC%B9%99

def div_conq(x, d, n):
	if n == 1:
		return x % d
	mod = div_conq(x, d, n//2)
	if n % 2:
		return (mod * mod * x) % d
	else:
		return (mod * mod) % d

def solution():
	x, n, d = map(int, input().split())
	print(div_conq(x, d, n))

if __name__ == "__main__":
	solution()
