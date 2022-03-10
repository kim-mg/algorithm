# 입력받은 정수 값들의 최대값과 최소값을 찾기
lst = list(map(int, input("정수값 입력 : ").split()))

max = lst[0]
min = lst[0]

for i in lst:
    if i > max:
        max = i
    if i < min:
        min = i

print(max, min)