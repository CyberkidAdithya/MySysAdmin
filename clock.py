from tkinter import Tk, Label
from time import strftime
import time

class clock_obj(Tk):
	def __init__(self):
		super().__init__()
		self.title("Clock")
		self.label1 =  Label(self, font=("ds-digital", 80), background = "black", foreground = "cyan")
		self.label1.pack(anchor='center')
		def time():
			string = strftime('%I:%M:%S %p')
			self.label1.config(text=string)
			self.label1.after(1000, time)
		time()
		self.after(5000, lambda: self.destroy())
		self.mainloop()
	pass


# print("Loading Clock...")	# debug checkpoint 1
# x = clock_obj()
# print("Closing Clock---")	# debug checkpoint 2
# x.mainloop()


#----------BACKUP FUNCTION----------

# from tkinter import Tk, Label
# from time import strftime

# def run1():
# 	root = Tk()
# 	root.title("Clock")
# 	label =  Label(root, font=("ds-digital", 80), background = "black", foreground = "cyan")
# 	label.pack(anchor='center')
# 	def time():
# 		string = strftime('%I:%M:%S %p')
# 		label.config(text=string)
# 		label.after(1000, time)
# 	time()

# 	root.mainloop()
# run1()