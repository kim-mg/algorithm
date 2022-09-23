import sys
from collections import deque
input = sys.stdin.readline

def solution():
	n = int(input())
	r = ""

	for _ in range(n):
		c = input().strip()
		s = int(input())
		e = 0
		l = input().strip("[]\n").split(',')
		if l[0] != '':
			dq_f = deque(list(l))
			dq_r = dq_f.copy()
			dq_r.reverse()
		else:
			dq_f = deque([])
			dq_r = dq_f.copy()
			dq_r.reverse()
		f = 0

		for cm in c:
			if cm == 'R':
				f = 1 if f == 0 else 0
			if cm == 'D':
				if not s:
					r += "error" + "\n"
					e = 1
					break
				if f:
					dq_f.pop()
					dq_r.popleft()
				else:
					dq_f.popleft()
					dq_r.pop()
				s -= 1
		if not e:
			if f:
				r += "[" + ','.join(list(dq_r)) + "]\n"
			else:
				r += "[" + ','.join(list(dq_f)) + "]\n"
	print(r.rstrip("\n"))

# ================================================================
# best time
def solve():

    for _ in range(int(input())):
        # 'RR' 는 안뒤집는 것과 동일하므로 ''로 바꿔준다
        p = [*map(len, input()[:-1].replace('RR', '').split('R'))]

        n = int(input())
        arr = input()[1:-2].split(',')
        # [left, right) 가 출력된다
        left, right = sum(p[::2]), n - sum(p[1::2])

        if left <= right:
            # len(p) % 2 == 1 인 경우 왼쪽에서 오른쪽 방향
            arr = arr[left:right] if len(p) % 2 else reversed(arr[left:right])
            print(f"[{','.join(arr)}]")
        else:
            print('error')

if __name__ == "__main__":
	solution()
