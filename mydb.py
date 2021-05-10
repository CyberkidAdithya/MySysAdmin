import getpass, subprocess, sys, time
from tkcalendar import Calendar, DateEntry
import pandas as pd
import mysql.connector as SQLconnector
import tkinter as tk
import tkinter.messagebox as mb
import tkinter.ttk as ttk

from encrypt import crypto
from sysinfo import *
from filescan import *
# from autoIDS import *

class DesktopApp(tk.Tk):	#root class
	def __init__(self):
		super().__init__()
		self.title("Desktops Management System")
		self.geometry("840x640+640+200")		#scrn_length*scrn_breadth+scrnXpos+scrnYpos


		#LABELS
		self.lblTitle = self.newLabel("Desktops Management System")
		self.lblTitle.configure(font=("Helvetica", 16), bg = "yellow", fg = "green", relief="ridge")
		self.lblName = self.newLabel("UserName: ")
		self.lblCPU = self.newLabel("CPU Usage: ")
		self.lblDisk = self.newLabel("Disk Storage: ")
		self.lblLocal = self.newLabel("Localhost: ")
		self.lblNet = self.newLabel("Network Status: ")
		self.lblMemo = self.newLabel("Memory Usage: ")
		self.lblDate = self.newLabel("Select Date: ")
		self.lblSelect = self.newLabel("Please select one record to update or delete")
		self.lblSearch = self.newLabel("Please enter System ID: ")


		#ENTRIES
		self.entName = self.newEntry()
		self.entCPU = self.newEntry()
		self.entDisk = self.newEntry()
		self.entLocal = self.newEntry()
		self.entNet = self.newEntry()
		self.entMemo = self.newEntry()
		self.entSearch = self.newEntry()


		self.entDate = DateEntry(self, width=12, background='darkblue', foreground='white', borderwidth=2, year=2021,locale='en_US', date_pattern='y-mm-dd')


		#BUTTONS
		self.btnRegister = self.newButton("Register")
		self.btnRegister.configure(command = self.register_desktop)
		self.btnUpdate = self.newButton("Update")
		self.btnUpdate.configure(command = self.update_desktop)
		self.btnDelete = self.newButton("Delete")
		self.btnDelete.configure(command = self.delete_desktop_data)
		self.btnClear = self.newButton("Clear")
		self.btnClear.configure(command = self.clear_form)
		self.btnShowAll = self.newButton("Show All")
		self.btnShowAll.configure(command = self.load_desktop_data)
		self.btnSearch = self.newButton("Search")
		self.btnSearch.configure(command = self.show_search_record)
		self.btnExit = self.newButton("Exit")
		self.btnExit.configure(command = self.exit)


		#TABLE(TREEVIEW)
		# style.configure("tableStyle1", anchor='center')
		# style.configure("tableStyle2", anchor='center', stretch=True )
		style = ttk.Style()
		style.configure("Treeview.heading", anchor='center')
		style.configure("Treeview.column", anchor='center', stretch=True)
		columns = ("#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8")
		self.tvDesktop= ttk.Treeview(self,show="headings",height="50", columns=columns)
		self.tvDesktop.heading('#1', text='DeskID')
		self.tvDesktop.column('#1', width=10)
		self.tvDesktop.heading('#2', text='UserName')
		self.tvDesktop.column('#2', width=10)
		self.tvDesktop.heading('#3', text='Processor')
		self.tvDesktop.column('#3',width=12)
		self.tvDesktop.heading('#4', text='Storage')
		self.tvDesktop.column('#4',width=12)
		self.tvDesktop.heading('#5', text='Localhost')
		self.tvDesktop.column('#5',width=12)
		self.tvDesktop.heading('#6', text='Network')
		self.tvDesktop.column('#6', width=12)
		self.tvDesktop.heading('#7', text='Memory')
		self.tvDesktop.column('#7', width=12)
		self.tvDesktop.heading('#8', text='Date')
		self.tvDesktop.column('#8', width=10)


        #SCROLL BARS
		vsb= ttk.Scrollbar(self, orient=tk.VERTICAL,command=self.tvDesktop.yview)
		vsb.place(x=40 + 640 + 1, y=310, height=180 + 20)
		self.tvDesktop.configure(yscroll=vsb.set)
		hsb = ttk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.tvDesktop.xview)
		hsb.place(x=40 , y=310+200+1, width=620 + 20)
		self.tvDesktop.configure(xscroll=hsb.set)
		self.tvDesktop.bind("<<TreeviewSelect>>", self.show_selected_record)


        #LABELS
		self.lblTitle.place(x=270, y=27,  height=30, width=300)
		style.configure("Label.place", height=25, width=125)
		self.lblName.place(x=30, y=70)
		self.lblCPU.place(x=30, y=115)
		self.lblDisk.place(x=30, y=160)

		self.lblLocal.place(x=410, y=70)
		self.lblNet.place(x=410, y=115)
		self.lblMemo.place(x=410, y=160)

		self.lblDate.place(x=30, y=205)
		self.lblSearch.place(x=30, y=560, height=25, width=225)
		self.lblSelect.place(x=166, y=290, height=20, width=436)


        #ENTRIES
		style.configure("Entry.place", height=25, width=225)
		self.entName.place(x=170, y=70)
		self.entCPU.place(x=170, y=115)
		self.entDisk.place(x=170, y=160)

		self.entLocal.place(x=550, y=70)
		self.entNet.place(x=550, y=115)
		self.entMemo.place(x=550, y=160)

		self.entDate.place(x=170, y=205)
		self.entSearch.place(x=270, y=560)


        #BUTTONS
		style.configure("Button.place", height=25, width=106)
		self.btnUpdate.place(x=98, y=250)
		self.btnDelete.place(x=234, y=250)
		self.btnRegister.place(x=370, y=250)
		self.btnClear.place(x=506, y=250)
		self.btnShowAll.place(x=642, y=250)
		self.btnSearch.place(x=505, y=558, height=45, width=114)
		self.btnExit.place(x=649, y=558, height=45, width=114)



		self.tvDesktop.place(x=40, y=310, height=200, width=640)
		self.create_table()
		self.load_desktop_data()


	def clear_form(self):
		self.entName.delete(0, tk.END)
		self.entCPU.delete(0, tk.END)
		self.entDisk.delete(0, tk.END)
		self.entLocal.delete(0, tk.END)
		self.entNet.delete(0, tk.END)
		self.entMemo.delete(0, tk.END)
		self.entDate.delete(0, tk.END)


	def exit(self):
		MsgBox = mb.askquestion('Exit Application', 'Are you sure you want to exit the application?', icon='warning')
		if MsgBox == 'yes':
			self.destroy()


	def delete_desktop_data(self):
		MsgBox = mb.askquestion('Delete Record', 'Are you sure! you want to delete selected desktop record?', icon='warning')
		if MsgBox == 'yes':
			if DBconnection.is_connected() == False:
				DBconnection.connect()
		DBcursor.execute("USE Desktop")  # Interact with  Database
		# deleteing selected Desktop record
		Delete = "DELETE FROM Desktop_master WHERE deskno='%s'" % (Desk_Number)
		DBcursor.execute(Delete)
		DBconnection.commit()
		mb.showinfo("Information", "Desktop Record Deleted Succssfully")
		self.load_desktop_data()
		self.entName.delete(0, tk.END)
		self.entCPU.delete(0, tk.END)
		self.entDisk .delete(0, tk.END)
		self.entLocal.delete(0, tk.END)
		self.entNet.delete(0, tk.END)
		self.entMemo.delete(0, tk.END)
		self.entDate.delete(0, tk.END)


	def create_table(self):
		if DBconnection.is_connected() == False:
			DBconnection.connect()
		# executing cursor with execute method and pass SQL query
		DBcursor.execute("CREATE DATABASE IF NOT EXISTS Desktop")  # Create a Database named Desktop
		DBcursor.execute("USE Desktop")  # Interact with Desktop Database
		# creating required tables
		DBcursor.execute("CREATE TABLE IF NOT EXISTS Desktop_master(Id INT(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,deskno INT(15),uname VARCHAR(30),CPU VARCHAR(30), disk VARCHAR(30), localhost VARCHAR(30),network VARCHAR(30), memory VARCHAR(30), joindate DATE)AUTO_INCREMENT=1")
		DBconnection.commit()


	def register_desktop(self):
		if DBconnection.is_connected() == False:
			DBconnection.connect()
		name_data = self.entName.get()
		CPU_data = self.entCPU.get()
		disk_data = self.entDisk.get()
		local_data = self.entLocal.get()
		network_data = self.entNet.get()
		memory_data = self.entMemo.get()
		date_data = self.entDate.get()

		#ALERT USER FOR EMPTY FIELDS
		if name_data == "":
			mb.showinfo('Information', "Please Enter Name")
			self.entName.focus_set()
			return
		if CPU_data == "":
			mb.showinfo('Information', "Please Enter CPU Stat")
			self.entCPU.focus_set()
			return
		if disk_data == "":
			mb.showinfo('Information', "Please Enter Disk Stat")
			self.entDisk.focus_set()
			return
		if local_data == "":
			mb.showinfo('Information', "Please Enter Localhost Stat")
			self.entLocal.focus_set()
			return
		if network_data == "":
			mb.showinfo('Information', "Please Enter Network Stat")
			self.entNet.focus_set()
			return
		if memory_data == "":
			mb.showinfo('Information', "Please Enter Memory Stat")
			self.entMemo.focus_set()
			return
		if date_data == "":
			mb.showinfo('Information', "Please Enter the Date")
			self.entDate.focus_set()
			return


		# Inserting record into Desktop_master table of Desktop database
		try:
			deskno = int(self.fetch_max_desk_no())
			print("New Desktop Id: " + str(deskno))
			query2 = "INSERT INTO Desktop_master (deskno, uname, CPU, disk, localhost, network, memory, joindate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
			# implement query Sentence
			DBcursor.execute(query2, (deskno, name_data, CPU_data, disk_data, local_data, network_data, memory_data, date_data))
			mb.showinfo('Information', "Desktop Registration Successfully")
			# Submit to database for execution
			DBconnection.commit()
			self.load_desktop_data()
		except mysql.connector.Error as err:
			print(err)
			# Rollback in case there is any error
			DBconnection.rollback()
			mb.showinfo('Information', "Data Insertion Failed!!!")
		finally:
			DBconnection.close()


	def automate_register_desktop(self):
		if DBconnection.is_connected() == False:
			DBconnection.connect()
		name_data = get_user()
		CPU_data = float(check_cpu_usage())
		disk_data = float(check_disk_usage("/"))
		local_data = "Good" if check_localhost() else "Bad"
		network_data = "Good" if check_connectivity() else "Bad"
		memory_data = float(check_memory())
		date_data = get_date()

		#ALERT USER FOR EMPTY FIELDS
		if name_data == "":
			mb.showinfo('Information', "Please Enter Name")
			self.entName.focus_set()
			return
		if CPU_data == "":
			mb.showinfo('Information', "Please Enter CPU Stat")
			self.entCPU.focus_set()
			return
		if disk_data == "":
			mb.showinfo('Information', "Please Enter Disk Stat")
			self.entDisk.focus_set()
			return
		if local_data == "":
			mb.showinfo('Information', "Please Enter Localhost Stat")
			self.entLocal.focus_set()
			return
		if network_data == "":
			mb.showinfo('Information', "Please Enter Network Stat")
			self.entNet.focus_set()
			return
		if memory_data == "":
			mb.showinfo('Information', "Please Enter Memory Stat")
			self.entMemo.focus_set()
			return
		if date_data == "":
			mb.showinfo('Information', "Please Enter the Date")
			self.entDate.focus_set()
			return


		# Inserting record into Desktop_master table of Desktop database
		try:
			deskno = int(self.fetch_max_desk_no())
			print("New Desktop Id: " + str(deskno))
			query2 = "INSERT INTO Desktop_master (deskno, uname, CPU, disk, localhost, network, memory, joindate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
			# implement query Sentence
			DBcursor.execute(query2, (deskno, name_data, CPU_data, disk_data, local_data, network_data, memory_data, date_data))
			mb.showinfo('Information', "Desktop Registration Successfully")
			# Submit to database for execution
			DBconnection.commit()
			self.load_desktop_data()
		except mysql.connector.Error as err:
			print(err)
			# Rollback in case there is any error
			DBconnection.rollback()
			mb.showinfo('Information', "Data Insertion Failed!!!")
		finally:
			DBconnection.close()


	def fetch_max_desk_no(self):
		if DBconnection.is_connected() == False:
			DBconnection.connect()
		DBcursor.execute("USE Desktop")  # Interact with desktop Database
		deskno  = 0
		query1 = "SELECT deskno FROM Desktop_master order by  id DESC LIMIT 1"
		# implement query Sentence
		DBcursor.execute(query1)  # Retrieving maximum desktop id no
		print("No of Records Fetched:" + str(DBcursor.rowcount))
		if DBcursor.rowcount == 0:
			deskno = 1
		else:
			rows = DBcursor.fetchall()
			for row in rows:
				deskno = row[0]
			deskno = deskno + 1
		print("Max desktop Id: " + str(deskno))
		return deskno


	def show_search_record(self):
		if DBconnection.is_connected() == False:
			DBconnection.connect()
		s_desk_no = self.entSearch.get()
		print(s_desk_no)
		if s_desk_no == "":
			mb.showinfo('Information', "Please Enter Desktop Number")
			self.entSearch.focus_set()
			return
		self.tvDesktop.delete(*self.tvDesktop.get_children())
		DBcursor.execute("USE Desktop")
		query3 = "SELECT deskno, uname, CPU, disk, localhost, network, memory, date_format(joindate,'%d-%m-%Y') FROM Desktop_master WHERE deskno='" + s_desk_no + "'"
		DBcursor.execute(query3)
		total = DBcursor.rowcount
		print("Total Desktops : " + str(total))
		rows = DBcursor.fetchall()

		Desk_No = ""
		User_Name = ""
		CPU_Stat = ""
		disk_Stat = ""
		local_Stat = ""
		net_Stat = ""
		memo_Stat = ""
		date_Stat = ""

		for row in rows:
			Desk_No = row[0]
			User_Name = row[1]
			CPU_Stat = row[2]
			disk_Stat = row[3]
			local_Stat = row[4]
			net_Stat = row[5]
			memo_Stat = row[6]
			date_Stat = row[7]
			print("Desk Number: "+str(Desk_No))
			self.tvDesktop.insert("", 'end', text=Desk_No, values=(Desk_No, User_Name, CPU_Stat, disk_Stat, local_Stat, net_Stat, memo_Stat, date_Stat))

	def show_selected_record(self,event):
		global item
		self.clear_form()
		for selection in self.tvDesktop.selection():
			item = self.tvDesktop.item(selection)
		global Desk_Number
		Desk_Number, PCname, PCcpu, PCdisk, PClocal, PCnet, PCmem, PCdate =  item["values"][0:8]
		self.entName.insert(0,PCname)
		self.entCPU.insert(0,PCcpu)
		self.entDisk.insert(0,PCdisk)
		self.entLocal.insert(0,PClocal)
		self.entNet.insert(0,PCnet)
		self.entMemo.insert(0,PCmem)
		self.entDate.insert(0,PCdate)
		return Desk_Number


	def update_desktop(self):
		if DBconnection.is_connected() == False:
			DBconnection.connect()
		print("Updating")
		DBcursor.execute("USE Desktop")
		User_Name = self.entName.get()
		CPU_Stat = self.entCPU.get()
		disk_Stat = self.entDisk.get()
		local_Stat = self.entLocal.get()
		net_Stat = self.entNet.get()
		memo_Stat = self.entMemo.get()
		date_Stat = self.entDate.get()
		print(Desk_Number)
		query4 = "UPDATE Desktop_master SET uname='%s', CPU='%s', disk='%s', localhost='%s', network='%s', memory='%s', joindate='%s' WHERE deskno='%s'" % (User_Name, CPU_Stat, disk_Stat, local_Stat, net_Stat, memo_Stat, date_Stat, Desk_Number)
		DBcursor.execute(query4)
		DBconnection.commit()
		mb.showinfo("Info", "Selected Desktop Record Updated Successfully ")
		self.load_desktop_data()

	def load_desktop_data(self):
		if DBconnection.is_connected() == False:
			DBconnection.connect()
		self.entDate.delete(0, tk.END)
		self.tvDesktop.delete(*self.tvDesktop.get_children())
		DBcursor.execute("USE Desktop")
		query5 = "SELECT deskno, uname, CPU, disk, localhost, network, memory, date_format(joindate,'%d-%m-%Y') FROM Desktop_master"
		DBcursor.execute(query5)
		total = DBcursor.rowcount
		#if total ==0:
			#mb.showinfo("Info", "Nothing To Display,Please add data")
			#return
		print("Total Data Entries:" + str(total))
		rows = DBcursor.fetchall()

		Desk_No = ""
		User_Name = ""
		CPU_Stat = ""
		disk_Stat = ""
		local_Stat = ""
		net_Stat = ""
		memo_Stat = ""
		date_Stat = ""

		for row in rows:
			Desk_No = row[0]
			User_Name = row[1]
			CPU_Stat = row[2]
			disk_Stat = row[3]
			local_Stat = row[4]
			net_Stat = row[5]
			memo_Stat = row[6]
			date_Stat = row[7]

			self.tvDesktop.insert("", 'end', text=Desk_No, values=(Desk_No, User_Name, CPU_Stat, disk_Stat, local_Stat, net_Stat, memo_Stat, date_Stat))

	def newLabel(self, myText):
		return tk.Label(text = myText, font=("Helvetica", 10), bg="blue", fg="yellow")

	def newButton(self, myText):
		return tk.Button(text = myText, font=("Helvetica", 11), bg="yellow", fg="blue")

	def newEntry(self):
		return tk.Entry(self)

print("Let's train the IDS and update PC first!")
try:
	print("Enter your username")
	SQLuname = str(input("Username:"))
	print("Enter your password")
	SQLpassword = str(getpass.getpass())
	print(str(crypto(SQLuname, "E"))+" : "+str(crypto(SQLpassword, "E")))
	DBconnection = SQLconnector.connect(
		host = "localhost",
		user = SQLuname,
		password = SQLpassword,
		database = "Desktop")
	DBcursor = DBconnection.cursor(buffered=True)
	print("my-SQL Login Successful")
	sql_query = pd.read_sql_query(
		'''select joindate, CPU, disk, memory from Desktop.Desktop_master'''
	,DBconnection)
	df = pd.DataFrame(sql_query)
	df.to_csv (r'usrstats.csv', index = False)
except Exception as e:
	print(e)
	print("my-SQL Login Failed! Please try again.")

print("Loading Admin Panel...")

try:
	time.sleep(3)
	app = DesktopApp()
	app.automate_register_desktop()
	app.mainloop()
except Exception as e:
	print(e)
	print("Desktop Management System failed to load")
	exit()

print("Closed DB")

checkForSignatures()