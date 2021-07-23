import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="14122017",
    database="maktab"

)
# jdvallarni ko'rish

baza = mydb.cursor()

baza.execute("show tables")

for i in baza:
    print(i)

# jadval yaratish

