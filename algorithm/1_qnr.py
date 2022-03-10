# 주어진 n을 나눈 몫과 나머지가 같은 수 찾기
def sol(n):
    rst = 0
    if n == 1:
        return 0
    # x / n = y
    # x % n = y
    for i in range(1, n):
        rst += (n + 1) * i

    return rst

if __name__ == "__main__":
    print(sol(100))