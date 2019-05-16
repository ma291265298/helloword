def oulashai(r):  # 欧拉筛法
    # 返回小于r的素数列表
    prime = [0 for i in range(r + 1)]  # 全部初始化为0
    common = []  # 存放素数
    for i in range(2, r + 1):
        if prime[i] == 0:
            common.append(i)
        for j in common:
            if i * j > r:
                break
            prime[i * j] = 1
            if i % j == 0:
                break;
    return common


m, n = [int(x) for x in input().split()]
prime = oulashai(120000)
flag = 0
for i in range(m - 1, n):
    if i == n - 1:
        print(prime[i])
    elif flag == 9:
        print(prime[i])
        flag = 0
    else:
        print(prime[i], end=' ')
        flag += 1
# print(flag)
