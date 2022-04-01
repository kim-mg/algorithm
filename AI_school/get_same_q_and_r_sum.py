import time
start = time.time()

def get_same_q_and_r_sum(n):
    res = 0
    # 시간복잡도에서의 차이
    for i in range(1, n**2):
        if (i // n) == (i % n):
            res += i

    # 보다 시간복잡도가 빠른 알고리즘
    # for i in range(1, n):
    #     res += (i * n) + i

    return res

print(get_same_q_and_r_sum(1000))
print("time :", time.time() - start)