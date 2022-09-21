import sys
input = sys.stdin.readline

n = int(input())
l = []
dic = dict([[x, 0] for x in range(-4000, 4001)])

for _ in range(n):
    m = int(input())
    l.append(m)
    dic[m] += 1

s_l = sorted(l)
s_d = sorted(dic.items(), key=lambda x: x[1], reverse=True)

print(int(round(sum(s_l)/len(s_l))))
print(s_l[len(s_l)//2])
if s_d[0][1] == s_d[1][1]:
    print(s_d[1][0])
else:
    print(s_d[0][0])
print(s_l[-1] - s_l[0])

######################################################################
# best
import sys
input = sys.stdin.readline

n = int(input())
l = [0] * 8001
s = 0
for _ in range(n):
    m = int(input())
    s += m
    l[m+4000] += 1

m_c = max(l)
mode = 0
mode_cnt = 0
idx = 0
med = None
min_n = 4000
max_n = -4000
for i in range(8001):
    i_c = l[i]
    if i_c == 0:
        continue

    num = i - 4000
    if i_c == m_c and mode_cnt < 2:
        mode = num
        mode_cnt += 1
    min_n = min(min_n, num)
    max_n = max(max_n, num)
    idx += l[i]
    if idx >= n//2+1 and med == None:
        med = num

print(round(s/n), med, mode, max_n - min_n, sep='\n')