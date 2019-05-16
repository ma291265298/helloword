a, b, c, d = map(int, input().split())
e = '0'
f = '0'
while a / 10 > 0:
    if a % 10 == b:
        e = e + str(b)
    a = int(a / 10)
while c / 10 > 0:
    if c % 10 == d:
        f = f + str(d)
    c = int(c / 10)
print(int(e)+int(f))
