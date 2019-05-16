import re

dict = {'A': 'MON', 'B': 'TUE', 'C': 'WED', 'D': 'THU', 'E': 'FRI', 'F': 'SAT', 'G': 'SUN'}
a = input()
b = input()
c = input()
d = input()
lista = list(a)
listb = list(b)
listc = list(c)
listd = list(d)
n = len(lista)
m = len(listc)
flag = 0
if len(lista) > len(listb):
    n = len(listb)
for i in range(n):
    if lista[i] == listb[i] and re.match('[A-N]|[0-9]', listb[i]) and flag == 1:
        # print(listb[i])
        if re.match('[A-N]', listb[i]):
            hour = 9 + ord(listb[i]) - ord('A') + 1
        else:
            hour = '0' + listb[i]
        break
    if lista[i] == listb[i] and re.match('[A-G]', listb[i]):
        # print(listb[i])
        DAY = listb[i]
        flag = 1
        continue
if len(listc) > len(listd):
    m = len(listd)
for j in range(m):
    if listc[j] == listd[j] and re.match('[a-z]|[A-Z]', listc[j]):
        # print(j)
        if 0 <= j <= 9:
            minute = '0' + str(j)
        else:
            minute = j
        break
print(dict[DAY], '{0}:{1}'.format(hour, minute))
