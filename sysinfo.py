import datetime, psutil, requests, shutil, socket, sys

def check_connectivity():    #bool
	request = requests.get("https://www.google.com")
	responseToday = request.status_code
	return responseToday == 200

def check_cpu_usage():    #float percent
	cpuToday = psutil.cpu_percent()
	return round(cpuToday,2)

def check_disk_usage(disk):    #float percent
	du = shutil.disk_usage(disk)
	freeToday = du.free / du.total * 100
	return round(freeToday,2)

def check_localhost():    #bool
	localhost = socket.gethostbyname('localhost')
	return localhost == '127.0.0.1'

def check_memory():    #float percent
	memory = psutil.virtual_memory()
	memoryToday = memory.percent
	return round(memoryToday,2)

def get_user():    #string username
	user = psutil.users()
	return str(user[0][0])

def get_time():    #string time
	timeToday = datetime.datetime.now().strftime("%I:%M:%S")
	return timeToday

def get_date():    #string date
	DateToday = str(datetime.date.today())
	return DateToday

def GUI_stats():
	from main import QApplication, SplashScreen
	app = QApplication(sys.argv)
	window = SplashScreen()
	app.exec_()
	QApplication.closeAllWindows()
	return "Window Closed"