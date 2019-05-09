import openpyxl

dic = {'A': 95, 'B': 85, 'C': 75, 'D': 65, 'E': 0}
wb = openpyxl.load_workbook('作业成绩.xlsx')
sheet1 = wb['平时作业 ']
# classes = sheet1.cell(2, 1).value
# _, number = str(classes).split('：')
# number = int(number)
for i in range(5, sheet1.max_row - 1):
    grade = 0
    for j in range(4, 12):
        grades = str(sheet1.cell(i, j).value)
        grade += dic[grades]
    avegrade = float(grade / 8)
    sheet1.cell(i, 12).value = avegrade

wb.save('2901作业成绩.xlsx')
