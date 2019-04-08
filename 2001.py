class Student:
    stu = []

    def _init_(self):
        stu = []

    def Insert(self, id, name, sex, year, month, day, chinese, math, english):
        print('Insert:')
        for x in range(len(self.stu)):
            if self.stu[x][0] == id:
                print('Failed')
                break
        else:
            chinese = int(chinese * 10) / 10
            math = int(math * 10) / 10
            english = int(english * 10) / 10
            s = chinese + math + english
            ave = round(s / 3 * 10) / 10
            self.stu.append([id, name, sex, year, month, day, str(chinese), str(math), str(english), str(ave), str(s)])
            # print(self.stu[-1])
            print(' '.join(self.stu[-1]))

    def List(self):
        print('List:')
        for x in range(len(self.stu)):
            print(' '.join(self.stu[x]))

    def Find(self, id):
        print('Find:')
        for x in range(len(self.stu)):
            if self.stu[x][0] == id:
                print(' '.join(self.stu[x]))
                break
        else:
            print('Failed')

    def Change(self, id, newname, newsex, newyear, newmonth, newday, newx, newy, newz):
        print('Change:')
        for x in range(len(self.stu)):
            if self.stu[x][0] == id:
                newx = int(newx * 10) / 10
                newy = int(newy * 10) / 10
                newz = int(newz * 10) / 10
                self.stu[x][1] = newname
                self.stu[x][2] = newsex
                self.stu[x][3] = newyear
                self.stu[x][4] = newmonth
                self.stu[x][5] = newday
                self.stu[x][6] = str(newx)
                self.stu[x][7] = str(newy)
                self.stu[x][8] = str(newz)
                self.stu[x][9] = str(round((newx + newy + newz) / 3 * 10) / 10)
                self.stu[x][10] = str(newx + newy + newz)
                print(' '.join(self.stu[x]))
                break
        else:
            print('Failed')

    def Delete(self, id):
        print('Delete:')
        for x in range(len(self.stu)):
            if self.stu[x][0] == id:
                del self.stu[x]
                print('Deleted')
                break
        else:
            print('Failed')

    def Sort(self, order):
        print("Sort:")
        if order == 'byid':
            self.stu = sorted(self.stu, key=lambda x: (x[0]))
            for x in range(len(self.stu)):
                print(' '.join(self.stu[x]))
        elif order == 'bybirthday':
            self.stu = sorted(self.stu, key=lambda x: (float(x[3]), float(x[4]), float(x[5])))
            for x in range(len(self.stu)):
                print(' '.join(self.stu[x]))
        elif order == 'bysum':
            self.stu = sorted(self.stu, key=lambda x: (float(x[9])))
            for x in range(len(self.stu)):
                print(' '.join(self.stu[x]))


stu = Student()
while (1):
    a = list(input().split())
    if a[0] == 'Insert':
        stu.Insert(a[1], a[2], a[3], a[4], a[5], a[6], float(a[7]), float(a[8]), float(a[9]))
    elif a[0] == 'Find':
        stu.Find(a[1])
    elif a[0] == 'List':
        stu.List()
    elif a[0] == 'Change':
        stu.Change(a[1], a[2], a[3], a[4], a[5], a[6], float(a[7]), float(a[8]), float(a[9]))
    elif a[0] == 'Delete':
        stu.Delete(a[1])
    elif a[0] == 'Sort':
        stu.Sort(a[1])
    elif a[0] == 'Quit' or a[0] == 'Exit':
        print('Good bye!')
        break
    else:
        pass
