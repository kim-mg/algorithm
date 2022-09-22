import sys
input = sys.stdin.readline

def random(n):
	if n == 0:
		return None
	return n

def main():
	if (ret := random(0)) is not None:
		print(ret)
	return 0

if __name__ == '__main__':
	main()