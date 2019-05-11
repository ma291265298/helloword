import openpyxl
import random
import pymysql
import os

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='root',
    db='python_student'
)

if not os.path.exists('python2900'):
    os.mkdir('python2900')

data = []
for x in range(50):
    wb = openpyxl.Workbook()
    sheet = wb.active
    for i in range(1, random.randint(0, 50)):
        temp = []
        for j in range(1, 6):
            lst = []
            for _ in range(30):
                k = random.randint(0, 2)
                if k == 0:
                    lst.append(chr(random.randint(ord('0'), ord('9'))))
                if k == 1:
                    lst.append(chr(random.randint(ord('A'), ord('Z'))))
                if k == 2:
                    lst.append(chr(random.randint(ord('a'), ord('z'))))

            sheet.cell(i, j).value = ''.join(lst)
            temp.append(''.join(lst))
        data.append(temp)
    wb.save('python2900/2900_excel_' + str(x) + '.xlsx')



try:
    with conn.cursor() as cursor:
        cursor = conn.cursor()
        sql = 'insert into excel(a, b, c, d, e)values (%s, %s, %s, %s, %s)'
        cursor.executemany(sql, data)
        conn.commit()
except pymysql.DatabaseError:
    print('插入失败')
    conn.rollback()
finally:
    conn.close()
