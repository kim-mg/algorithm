import sys
input = sys.stdin.readline

def fib(n):
	if (n == 1 or n == 2):
		return 1;  # 코드1
	return (fib(n - 1) + fib(n - 2))

def fibonacci(n):
	if 

if __name__ == "__main__":
	n = int(input())
	dp = { 0 : 0,
			1 : 1,}
	print(fib(n), fibonacci(n), sep=' ')
