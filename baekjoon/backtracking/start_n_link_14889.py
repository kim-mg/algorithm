import itertools
import sys
input = sys.stdin.readline

n = int(input())
s = [[0]]
p = itertools.permutations

for _ in range(n):
    s.append([0] + list(map(int, input().split())))

def get_score(team, s):
    rst = 0

    for tup in team:
        a = tup[0]
        b = tup[1]
        rst += s[a][b]

    return rst

def backtrack(team, size, s):
    global min_s
    if size > n/2:
        team_b = []
        for i in range(1, n+1):
            if i not in team:
                team_b.append(i)
        tmp_m = abs(get_score(p(team, 2), s) - get_score(p(team_b, 2), s))
        if min_s > tmp_m:
            min_s = tmp_m
        return

    for i in range(size, n+1):
        if size <= n/2 and i not in team:
            tmp_team = team.copy()
            tmp_team.append(i)
            if tmp_team[0] != 1:
                return
            backtrack(tmp_team, size + 1, s)
        else:
            return

min_s = 1000000000
backtrack([], 1, s)
print(min_s)

############################################################
# best

import itertools
import sys
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
c = itertools.combinations

rows_sum = [sum(row) for row in s]
cols_sum = [sum(col) for col in zip(*s)]
stat_by_member = [x + y for x, y in zip(rows_sum, cols_sum)]
total = sum(rows_sum)
min_score = min(abs(total - sum(stats)) for stats in c(stat_by_member, n//2))

print(min_score)