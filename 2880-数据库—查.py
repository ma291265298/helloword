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
        sql = 'select * from student where number>=1501 and number<=1509'
        cursor.execute(sql)
        lis = cursor.fetchall()
        for i in lis:
            print(i)
        conn.commit()

except pymysql.DatabaseError:
    print('查询失败')
    conn.rollback()
finally:
    conn.close()
