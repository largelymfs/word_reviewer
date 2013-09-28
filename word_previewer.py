import sys
import os
class WordPreviewer:
	def __init__(self):
		self.word={}
	def load(self, filename):
		self.file = filename
		try:
			f = open(filename,"r")
		except:
			print "opening "+filename+" error..."
			return
		content = f.read().split("\n")
		nownum = ""
		for line in content:
			if (line==""):
				continue
			if (line[0:4]=="Unit"):
				self.word.setdefault(line,{})
				nownum = line
			else:
				items = line.split("@")
				english = items[0]
				chinese = items[1]
				self.word[nownum].setdefault(english, chinese)
		f.close()
	def show(self, english, chinese):
		os.system("clear")
		print "\t"+english
		print "Next?:",
		sys.stdin.read(1)
		print "\t"+english+"   "+chinese
		sys.stdin.read(1)
		print 
	def display(self):
		now_units = 0
		now_para = 0
		buffers = {}
		shuffle = {}
		for (units, content) in self.word.items():
			print 
			print 
			print 
			print "\t\t\t" + units
			for (english, chinese) in content.items():
				self.show(english,chinese)
				buffers.setdefault(english,chinese)
			now_units = now_units + 1
			if (now_units==5):
				now_units = 0
				print
				print 
				print
				print "\t\t\t>>>>>>>>>>>>>>>>>>>>Shuffle in " + self.file+" Half<<<<<<<<<<<<<<<<<<<<"
				for (english, chinese) in buffers.items():
					self.show(english, chinese)
					shuffle.setdefault(english,chinese)
				buffers = {}
				now_para = now_para + 1
				if (now_para==2):
					now_para = 0
					print 
					print
					print
					print "\t\t\t>>>>>>>>>>>>>>>>>>>>Shuffle in " + self.file+" Whole<<<<<<<<<<<<<<<<<<<<"
					for (english, chinese) in shuffle.items():
						self.show(english, chinese)
					shuffle = {}
a = WordPreviewer()
a.load("List16.txt")
a.display()