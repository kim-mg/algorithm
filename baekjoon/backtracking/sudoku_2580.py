import sys
input = sys.stdin.readline

table = []
t_z = []

# 입력부
for i in range(9):
    l = list(map(int, input().split()))
    # 전체적인 테이블 : row 기준
    table.append(l)
    for j, v in enumerate(l):
        # row 기준 비어있는 좌표
        if v == 0:
            t_z.append([i,j])

# table의 숫자를 str로 변환
def itoa_arr(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = str(arr[i][j])
    return arr

# row & col & 33 체크
def check_xy_box(row, col):
    p_lst = [i for i in range(1, 10)]

    # row, col check
    for i in range(9):
        if table[row][i] in p_lst:
            p_lst.remove(table[row][i])
        if table[i][col] in p_lst:
            p_lst.remove(table[i][col])

    # 33 check
    r = row // 3
    c = col // 3
    for n in range(r*3, (r+1)*3):
        for m in range(c*3, (c+1)*3):
            if table[n][m] in p_lst:
                p_lst.remove(table[n][m])

    return p_lst

flag = 0
# 스도쿠 프로그램
def sudoku(cnt):
    global flag

    if flag:
        return
    
    if cnt == len(t_z):
        c_table = itoa_arr(table)
        print('\n'.join(map(' '.join, c_table)))
        flag = 1
        return
    else:
        row, col = t_z[cnt]
        positive_lst = check_xy_box(row, col)

        for n in positive_lst:
            table[row][col] = n
            sudoku(cnt + 1)
            table[row][col] = 0
    
sudoku(0)

######################################################################
# best

board = [list(input()) for _ in range(9)]

def cross(A, B):
    return [a+b for a in A for b in B]

digits = '123456789'
rows = 'ABCDEFGHI'
cols = digits

squares = cross(rows, cols)
unitlist = ([cross(rows, c) for c in cols] + [cross(r, cols) for r in rows] + [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')])
units = dict((s, [u for u in unitlist if s in u]) for s in squares)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in squares)

def grid_values(board):
    chars = []
    for l in board:
        temp = [c for c in l if c in digits or c in '0.']
        chars += temp
    return dict(zip(squares, chars))

def parse_grid(board):
    values = dict((s, digits) for s in squares)
    for s, d in grid_values(board).items():
        if d in digits and not assign(values, s, d):
            return False
    return values
    
def assign(values, s, d):
    other_values = values[s].replace(d, '')
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False

def eliminate(values, s, d):
    if d not in values[s]:
        return values
    values[s] = values[s].replace(d, '')
    if len(values[s]) == 0:
        return False
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
            return False
    for u in units[s]:
        dplaces = [s for s in u if d in values[s]]
        if len(dplaces) == 0:
            return False
        elif len(dplaces) == 1:
            if not assign(values, dplaces[0], d):
                return False
    return values

def display(values):
    width = 1+max(len(values[s]) for s in squares)
    for r in rows:
        print(' '.join(values[r+c] for c in cols))

def solve(board): return search(parse_grid(board))

def search(values):
    if values is False:
        return False
    if all(len(values[s]) == 1 for s in squares):
        return values
    n,s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    return some(search(assign(values.copy(), s, d)) for d in values[s]) 

def some(seq):
    for e in seq:
        if e: return e
    return False

display(solve(board))