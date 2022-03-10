a, b, R = map(int, input("a b R을 입력해주세요: ").split())
N = int(input("N을 입력해주세요: "))
for i in range(1, N+1):
    x, y = map(int, input("x y를 입력해주세요: ").split())
    if ((x-a)**2 + (y-b)**2) >= R**2:
        print("silent")
    else:
        print("noisy")