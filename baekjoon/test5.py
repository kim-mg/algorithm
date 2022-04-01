import sys
input = sys.stdin.readline

if __name__ == "__main__":
	x = int(input())
	sto = [0] * (x + 1)

	for i in range(2, x + 1):
		sto[i] = sto[i - 1] + 1
		if i % 3 == 0:
			sto[i] = min(sto[i], sto[i // 3] + 1)
		if i % 2 == 0:
			sto[i] = min(sto[i], sto[i // 2] + 1)
	print(sto[x])
