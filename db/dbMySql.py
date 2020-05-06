from flask_mysqldb import MySQLdb

db = MySQLdb.connect(
    user='geovane',
    password='1.618_3,14',
    db='TCC_development',
    host='localhost',
    port=3306
)

cursor = db.cursor()

cursor.execute('Select * from teste')
for usuario in cursor.fetchall():
    print(usuario[0])
