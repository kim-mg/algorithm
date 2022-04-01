n = int(input())
meet_list = []

for _ in range(n):
    meet_list.append(list(map(int, input().split())))


# 끝나는 시간이 같을 경우 시작 시간에 대한 정렬
meet_list.sort(key=lambda row : [row[1], row[0]])

result = 1
last_book_end_time = meet_list[0][1]

for idx in range(1, len(meet_list)):
    if last_book_end_time <= meet_list[idx][0]:
        result += 1
        last_book_end_time = meet_list[idx][1]

print(result)