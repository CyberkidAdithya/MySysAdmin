#------------------------------READ ME FIRST -------------------------------------------
'''
myBack ===> Database Connector
myCursor ===> Cursor
userData ===> Insertion Connector
loginSQL() ===> Func to login into mySQL
createDB() ===> Func to create database
showDB() ===> Func to show all databases
createTab() ===> Func to create table
showTab() ===> Func to show all tables
insertTab() ===> Func to insert new tables
showthisTab() ===> Func to view current table

'''

#-------------------CONNECTING TO MYSQL------------
import mysql.connector
myBack = mysql.connector.connect(host = "localhost",user = "root",passwd = "esadi1234", database = "testdb")
print("Logged into mySQL and connected to " + "testdb")
myCursor = myBack.cursor()	# adding a cursor in mySQL

#-----------------------------CREATING A DATABASE------------------------------
def createDB():
	try:
		myCursor.execute("CREATE DATABASE testdb")
	except mysql.connector.errors.DatabaseError:
		print("Database already exists. Skipping this step")
	except:
		print("Unknown error in Code")
	finally:
		print("Database is ready")
createDB()

def showDB():
	myCursor.execute("SHOW DATABASES")
	print("List of Available Databases: ")
	for db in myCursor:
		print(db)
showDB()

#----------------------------CREATING A TABLE-----------------------------------
def createTab():
	try:
		myCursor.execute("CREATE TABLE users (name VARCHAR(255), email VARCHAR(255), password VARCHAR(255), roll_no INTEGER AUTO_INCREMENT PRIMARY KEY)")
	except mysql.connector.ProgrammingError:
		print("Table already exists. Skipping this step")
	except:
		print("Unknown error in Code")
	finally:
		print("Table is ready")
createTab()

def showTab():
	myCursor.execute("SHOW TABLES")
	print("List of Available Tables")
	for table in myCursor:
		print(table)
showTab()

#-------------------INSERTING VALUES-----------------
def insertTab():
	userData = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
	record1 = ("Adithya", "cyberkid@gmail.com", "abc123!@#")
	record2 = ("VamaSoni", "vamasoni@gmail.com", "xyz987#@!")
	myCursor.execute(userData, record1)
	myCursor.execute(userData, record2)
	# myCursor.execute("USE testdb")
	myBack.commit()
	print("Inserted Records and performed Commit!")
insertTab()

#----------------------------------------MAIN PROGRAM----------------------------------------------
def showthisTab():
	print("Displaying Requested Table")
	myCursor.execute("SELECT * FROM users")	
	for user in myCursor:
		print(user)
showthisTab()
