# N의 약수 구하기
N = int(input("N : "))

f_lst = []
r_lst = []

sqrt = int(N**0.5)

for i in range(1, sqrt + 1):
    if i == sqrt:
        f_lst.append(i)
        continue
    if N % i == 0:
        f_lst.append(i)
        r_lst.append(int(N / i))

# while r_lst:
    # f_lst.append(r_lst.pop())

print(f_lst + r_lst[::-1])

# 지웅쓰
'''
# import math
num = int(input())

# sqrt_num = int(math.sqrt(num))
sqrt_num = int(num ** (1/2)) 

front_divisor_list = [] 
rear_divisor_list = [] 

for i in range(1, sqrt_num+1): 
    if num % i == 0: 
        front_divisor_list.append(i) 
        if i != int(num/i): 
            rear_divisor_list.append(int(num/i)) 

print(front_divisor_list + rear_divisor_list[::-1])
'''