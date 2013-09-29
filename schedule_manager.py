import sys
class ScheduleManager:
	def __init__(self, filename):
		self.dic = {}
		f = open(filename, "r")
		try:
			lines = f.read().split("\n")
			for line in lines:
				items = line.split(" ")
				date = items[0]
				if (len(date)<8):
					continue
				self.dic.setdefault(date,[])
				for item in items:
					if (item!=date):
						self.dic[date].append(item)
		except:
			print "There is an error in opening file..."
		finally:
			f.close()
	def add(self, new_date, new_list):
		if (new_date not in self.dic):
			self.dic.setdefault(new_date,[])
		self.dic[new_date].append(new_list)
	def plus(self, old, number):
		year = int(old[0:4])
		month = int(old[4:6])
		date = int(old[6:])
		date = date + number
		upper = 31
		if (month == 4 or month== 6 or month== 9 or month == 11):
			upper = 30
		if (month == 2):
			if (year %400==0 or (year % 4==0 and year % 100 !=0)):
				upper = 29
			else:
				upper = 28
		if (date>upper):
			date = date - upper
			month = month + 1
			if (month==13):
				month = 1
				year = year + 1
		tmp = str(year)
		if (month < 10):
			tmp = tmp + "0" + str(month)
		else:
			tmp = tmp + str(month)
		if (date < 10):
			tmp = tmp + "0" + str(date)
		else:
			tmp = tmp + str(date)
		return tmp

	def insert(self, new_date, new_list):
		self.add(new_date, new_list)
		new_date = self.plus(new_date, 1)
		self.add(new_date, new_list)
		new_date = self.plus(new_date, 2)
		self.add(new_date, new_list)
		new_date = self.plus(new_date, 4)
		self.add(new_date, new_list)
		new_date = self.plus(new_date, 7)
		self.add(new_date, new_list)
		new_date = self.plus(new_date, 15)
		self.add(new_date, new_list)
	def createfile(self, filename):
		f = open(filename,"w")
		try:
			keys = self.dic.keys()
			keys.sort()
			for k in keys:
				f.write(k)
				items = self.dic[k]
				items.sort()
				f.write(" "+items[0])
				for i in range(1, len(items)):
					if (items[i]!=items[i-1]):
						f.write(" "+items[i])
				f.write("\n")			
		finally:
			f.close()
a = ScheduleManager("schedule.txt")
date = sys.argv[1]
listname = sys.argv[2]
a.insert(date, listname)
a.createfile("schedule.txt")
