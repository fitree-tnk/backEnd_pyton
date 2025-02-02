import mysql.connector as mysqlcon
mydb = mysqlcon.connect (
    host = "localhost",
    user = "root",
    password = "271146",
    database = "shopping"
    )
print(mydb)