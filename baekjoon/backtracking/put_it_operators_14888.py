import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
opers = []

for i, op in enumerate(list(map(int, input().split()))):
    while op > 0:
        opers.append(i)
        op -= 1

def dfs(nums, opers, num_idx, res):
    rst = []
    if (num_idx == n):
        rst.append(res)
        return rst

    if (num_idx == 0):
        res = nums[num_idx]
        num_idx += 1

    for i, op in enumerate(opers):
        if op == -1:
            continue
        tmp = res
        tmp_idx = num_idx
        tmp_opers = opers.copy()
        if op == 0:
            tmp += nums[num_idx]
        elif op == 1:
            tmp -= nums[num_idx]
        elif op == 2:
            tmp *= nums[num_idx]
        elif op == 3:
            if tmp < 0:
                tmp = (-tmp // nums[num_idx]) * -1
            else:
                tmp = tmp // nums[num_idx]
        tmp_opers.pop(i)
        rst += dfs(nums, tmp_opers, tmp_idx + 1, tmp)
    return rst

r = dfs(nums, opers, 0, 0)

print(max(r))
print(min(r))

###############################################################
# best

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
opers = list(map(int, input().split()))

def backtrack(pre_val, idx, plus, minus, multi, divide):
    global max, min
    if idx == n:
        if max < pre_val:
            max = pre_val
        if min > pre_val:
            min = pre_val
    else:
        if plus:
            backtrack(pre_val + nums[idx], idx + 1, plus -1, minus, multi, divide)
        if minus:
            backtrack(pre_val - nums[idx], idx + 1, plus, minus -1, multi, divide)
        if multi:
            backtrack(pre_val * nums[idx], idx + 1, plus, minus, multi -1, divide)
        if divide:
            if pre_val < 0:
                backtrack( -(abs(pre_val) // nums[idx]), idx + 1, plus, minus, multi, divide -1)
            else:
                backtrack( pre_val // nums[idx], idx + 1, plus, minus, multi, divide -1)

max = -1000000001
min = 1000000001
backtrack(nums[0], 1, *opers)
print(max, min, sep='\n')
