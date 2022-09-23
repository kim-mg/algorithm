import sys
input = sys.stdin.readline

if __name__ == "__main__":
	n = int(input())
	l = []
	for _ in range(n):
		m = int(input())
		l.append(m) if m else l.pop()
	print(sum(l))

# =====================================================
# best time
import sys
input = sys.stdin.readline

if __name__ == "__main__":
	n = int(input())
	l = []
	for _ in range(n):
		m = int(input())
		l.append(m) if m else l.pop()
	print(sum(l))

