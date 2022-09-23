import sys
input = sys.stdin.readline

if __name__ == "__main__":
	num = int(input())
	lst = []
	store = []
	for _ in range(num):
		lst.append(int(input()))
	
	store.append(lst[0])
	if num > 1:
		store.append(max(lst[0] + lst[1], lst[1]))
	if num > 2:
		store.append(max(lst[0] + lst[2], lst[1] + lst[2]))
	for i in  range(3, num):
		store.append(max(store[i-2] + lst[i], store[i-3] + lst[i] + lst[i-1]))
	print(store.pop())