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
        sql = 'update student set name=%s where number=%s'
        date = [
            ('李炎黄', '1501'),
            ('吕萌', '1505'),
            ('石灰', '1509')
        ]
        cursor.executemany(sql, date)
        conn.commit()
        print('更新成功')
except pymysql.DatabaseError:
    print('更新失败')
    conn.rollback()
finally:
    conn.close()
