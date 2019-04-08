class Student:
    def __init__(self, number, name, sex, chinese, math, english):
        self.number = number
        self.name = name
        self.sex = sex
        self.chinese = chinese
        self.math = math
        self.english = english

    def run(self):
        s = self.chinese + self.math + self.english
        ave = s / 3
        print("{} {} {} {:.2f} {:.2f} {:.2f} {:.2f} {:.2f}"
              .format(self.number, self.name, self.sex, self.chinese, self.math, self.english, ave, s))


num, name, s, c, m, e = input().split()
student = Student(num, name, s, float(c), float(m), float(e))
student.run()
