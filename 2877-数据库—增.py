import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='root',
    db='python_student'
)

try:
    with conn.cursor() as cursor:
        sql = 'insert into student(number,name,sex,math,english,computer) values (%s,%s,%s,%s,%s,%s)'
        date = [
            ('1501', '炎黄', 'M', 78.5, 70.0, 100.0),
            ('1505', '吕萌萌', 'M', 100.0, 90.0, 95.0),
            ('1509', '石耀举', 'F', 60.5, 90.0, 70.0),

        ]
        cursor.executemany(sql, date)
        conn.commit()
        print('插入成功')
except pymysql.DatabaseError:
    print('插入失败')
    conn.rollback()
finally:
    conn.close()
