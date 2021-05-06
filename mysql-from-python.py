import os
import pymysql
if os.path.exists("env.py"):
    import env

password = os.environ.get('password')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password=password,
                             db='Chinook')


try:
    # Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # Close the connection, regardless of whether the above was successful or not
    connection.close()
