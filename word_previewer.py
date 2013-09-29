#!/usr/bin/env python
# -*- coding: utf-8 -*- 
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
				chineses = chinese.split('；')
				self.word[nownum].setdefault(english, chineses)

		f.close()
	def show(self, unit, english, chinese):
		os.system("clear")
		print "\t"+unit
		print "\t"+english
		print "Next?:",
		sys.stdin.read(1)
		for item in chinese:
			print "\t"+item
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
				self.show(units,english,chinese)
				buffers.setdefault(english,chinese)
			for (english, chinese) in content.items():
				self.show(units,english, chinese)
				buffers.setdefault(english, chinese)
			now_units = now_units + 1
			if (now_units==5):
				now_units = 0
				print
				print 
				print
				print "\t\t\t>>>>>>>>>>>>>>>>>>>>Shuffle in " + self.file+" Half<<<<<<<<<<<<<<<<<<<<"
				for (english, chinese) in buffers.items():
					self.show(units,english, chinese)
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
						self.show(units,english, chinese)
					shuffle = {}
filename = "data/"+sys.argv[1]+".txt"
a = WordPreviewer()
a.load(filename)
a.display()
