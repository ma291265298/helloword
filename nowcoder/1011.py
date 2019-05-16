lists = list(input())
for i in range(10):
    flag = 0
    for j in range(len(lists)):
        if i == int(lists[j]):
            flag += 1
        # print(lists[j])
    if flag == 0:
        continue
    print('{}:{}'.format(i, flag))
