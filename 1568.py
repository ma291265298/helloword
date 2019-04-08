class Student:
    stu = []

    def __init__(self):
        stu = []

    def Insert(self, id, name, sex, s1, s2, s3):
        self.s1 = '{:.2f}'.format(float(s1))
        self.s2 = '{:.2f}'.format(float(s2))
        self.s3 = '{:.2f}'.format(float(s3))
        su = '{:.2f}'.format(float(s1) + float(s2) + float(s3))
        ave = '{:.2f}'.format(float(su) / 3)
        self.stu.append([id, name, sex, self.s1, self.s2, self.s3, ave, su])
        print(' '.join(self.stu[-1]))

    def List(self):
        self.stu = sorted(self.stu, key=lambda x: int(x[0]))
        for x in range(len(self.stu)):
            print(' '.join(self.stu[x]))


stu = Student()
while (1):
    a = input().split()
    if a[0] == 'INSERT':
        stu.Insert(a[1], a[2], a[3], a[4], a[5], a[6])
    elif a[0] == 'LIST':
        stu.List()
    elif a[0] == 'QUIT':
        print('Good bye!')
        break
    else:
        pass
