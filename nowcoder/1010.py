n, d = input().split()
n = int(n)
d = float(d)
suhe = 0.0
sumo = 0.0
he = [float(x) for x in input().split()]
mo = [float(x) for x in input().split()]
ge = []
for i in range(n):
    ge.append((mo[i] / he[i], mo[i], he[i]))
ge = sorted(ge, key=lambda x: x[0], reverse=True)
for i in range(n):
    suhe = suhe + ge[i][2]
    sumo = sumo + ge[i][1]
    if suhe >= d:
        sumo = sumo - (ge[i][0] * (suhe - d))
        break
result = round(sumo * 100) / 100
print('{:.2f}'.format(result))
