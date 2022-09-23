import sys
input = sys.stdin.readline


n = int(input())
table = []
obj = [i for i in range(1, n+1)]

def check_q(v, t):
    cur_idx = len(t)
    for j, w in enumerate(t):
        check = cur_idx - j
        if v - check == w or v + check == w:
            return 0
    return 1

def n_queen_process(table, n, obj):
    cnt = 0
    cur_idx = len(table)
    if cur_idx == n:
        return 1

    for i, v in enumerate(obj):
        if check_q(v, table):
            # t = table.copy()
            # t.append(v)
            t = table
            t.append(v)
            o = obj.copy()
            o.pop(i)
            cnt += n_queen_process(t, n, o)
            if len(t) == 1 and n % 2 == 0 and i+1 == n//2:
                return cnt * 2
            if len(t) == 1 and n % 2 != 0:
                if i+1 == n//2:
                    cnt *= 2
                elif i+1 == (n//2) + 1:
                    return cnt
            t.pop()
    return cnt

print(n_queen_process(table, n, obj))

###############################################################
# best - ordinary

N = int(input())
ans = 0
col = [False] * N  # i번째 열에 퀸을 뒀는지
d1 = [False] * 2 * N  # \ 대각선, 우상단부터 0
d2 = [False] * 2 * N  # / 대각선, 좌상단부터 0


def backtracking(row):
    global ans
    if row == N:
        ans += 1
        return

    for j in range(N if row else N // 2):
        if not col[j] and not d1[row - j] and not d2[row + j]:
            col[j] = True
            d1[row - j] = True
            d2[row + j] = True

            backtracking(row + 1)

            d2[row + j] = False
            d1[row - j] = False
            col[j] = False


if N % 2:
    # 홀수일 때 첫번째 행에 퀸을 왼쪽 절반만 둬보고 그 때의 경우의 수를 2배로 취해준다 (정가운데 제외)
    backtracking(0)
    ans *= 2

    # 첫번째 행의 정가운데에 퀸을 뒀을 때의 경우의 수를 구해서 더해준다
    j = N // 2
    col[j] = d1[-j] = d2[j] = True
    backtracking(1)

    print(ans)
else:
    # 짝수일 때 첫번째 행에 퀸을 왼쪽 절반만 둬보고 그 떄의 경우의 수를 2배로 취해준다
    backtracking(0)
    print(ans * 2)

#######################################################################
# best2 - bit calculations

def search(col, ld, rd, n):
    size = ((1 << n) - 1)
    count = 0

    if col == size:
        return 1

    slots = ~(col | ld | rd) & size
    while slots:
        bit = slots & -slots
        count += search(col | bit, (ld | bit) >> 1, (rd | bit) << 1, n)
        slots -= bit
    return count


def solution(n):
    return search(0, 0, 0, n)


print(solution(int(input())))