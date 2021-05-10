import csv, datetime, pyautogui, os

def create_file(self, file_name):
	if os.path.exists(file_name):  # noqa: E111
		print("File already exists !")
	else:
		print("Creating new file", file_name + "...")
		file = open(file_name,"w")
		file.close()

def create_folder(self, folder_name):
	if os.path.isdir(folder_name):
		print("Folder already exists")
	else:
		print("Creating new folder",folder_name)
		os.mkdir(folder_name)

def delete_file(self, file_name):
	try:
		print("Deleting file", file_name + "...")
		os.remove(file_name)
	except Exception as e:
		print("Error:",e)

def delete_folder(self, folder_name):
	os.rmdir(folder_name)
	print("Deleted folder",folder_name)

def load_csv(self, file_name):
	f = open(file_name)
	csv_f = csv.reader(f)
	for row in csv_f:
		print(row)
		break
	f.close()

def modified_check(self, file_name):
	timestamp = os.path.getmtime(file_name) #UNIX timestamp
	print("Modified:",datetime.datetime.fromtimestamp(timestamp))

def screenshot(self):
		img = pyautogui.screenshot()
		img.save("report_img.png")