import mysql.connector

mydb = mysql.connector.connect(host='localhost',user='chakri',passwd='chakri',database='family')

mycursor=mydb.cursor()

mycursor.execute("select * from family.members")

#result=mycursor.fetchall()
result=mycursor.fetchone()

#for i in mycursor:
for i in result:
	print(i)


