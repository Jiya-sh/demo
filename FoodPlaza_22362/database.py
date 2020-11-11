import pymysql

mydatabase = pymysql.connect("localhost","root","root","foodplaza_22362")

mycursor = mydatabase.cursor()

if mydatabase is not None:
	print("Connected")