import sys
input = sys.stdin.readline

def solution():
	n = int(input())
	q = [0] * (n + 1)
	fr = [1, 0]
	line = []
	
	def push(n):
		fr[1] += 1
		q[fr[1]] = n
	
	def pop():
		if fr[1] < fr[0]:
			return '-1'
		fr[0] += 1
		return q[fr[0] - 1]

	def size():
		return str(fr[1] - (fr[0] - 1))

	def empty():
		if fr[1] < fr[0]:
			return '1'
		return '0'

	def front():
		if fr[1] < fr[0]:
			return '-1'
		return q[fr[0]]

	def back():
		if fr[1] < fr[0]:
			return '-1'
		return q[fr[1]]

	def queue(s):
		if len(s) > 1:
			if s[0] == 'push':
				push(s[1])
		if s[0] == 'pop':
			line.append(pop())
		if s[0] == 'size':
			line.append(size())
		if s[0] == 'empty':
			line.append(empty())
		if s[0] == 'front':
			line.append(front())
		if s[0] == 'back':
			line.append(back())

	for _ in range(n):
		queue(input().split())
	
	print('\n'.join(line))

# ===========================================================
# best time
# character comparsion method
def solve():
    q = [0]*2000000
    front = rear = 0
    res = []
    for string in sys.stdin.read().splitlines()[1:]:
        t = string[1]
        if t == "u":
            q[rear] = string[5:]
            rear += 1
        elif t == "o":
            if front == rear:
                res.append('-1')
            else:
                res.append(q[front])
                front += 1
        elif t == "i":
            res.append(str(rear-front))
        elif t == "m":
            res.append('1' if front == rear else '0')
        elif t == "r":
            res.append(q[front] if front != rear else '-1')
        elif t == "a":
            res.append(q[rear-1] if front != rear else '-1')

    sys.stdout.write('\n'.join(res))

if __name__ == "__main__":
	solution()