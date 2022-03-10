# 좌표 (a, b)로부터 반경 R 기준으로 조용한 공간 찾기
a, b, R = map(int, input("a b R을 입력해주세요: ").split())
N = int(input("N을 입력해주세요: "))
for i in range(1, N+1):
    x, y = map(int, input("x y를 입력해주세요: ").split())
    if ((x-a)**2 + (y-b)**2) >= R**2:
        print("silent")
    else:
        print("noisy")

# 지웅쓰 답안
'''
def check_sound_status(a,b,r,x,y):
    if (x-a)**2 + (y-b)**2 >= r**2:
        return "silent"
    return "noisy"

a, b, r = map(int, input().split())
n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    print(check_sound_status(a,b,r,x,y))
'''