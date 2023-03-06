import pymysql
import pymysql.cursors 

connection = pymysql.connect(
    host="10.100.33.60",
    user="mwilliams",
    password="220467419",
    database="world",
    cursorclass=pymysql.cursors.DictCursor,
    autocommit=True
)
cursor = connection.cursor()
cursor = connection.cursor("SELECT * FROM `country`")

result = cursor.fetchone()

print(result)