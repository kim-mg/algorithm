lst = [[0,1] for _ in range(3)]
for i in range(3):
    lst[i][0] += i
    print(lst[i][0], i)
print(lst)