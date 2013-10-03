import os
def clear():
	os.system("clear")
def print_review():
	clear()
	print ">Please input the List Number..."
	while 0==0:
		try:
			print ">",
			num = int(raw_input())
			break
		except:
			print ">Please input again..."
	os.system("python word_previewer.py List"+str(num))
def print_add():
	clear()
	print ">Plase input the List Number..."
	while 0==0:
		try:
			print ">",
			num = int(raw_input())
			break
		except:
			print ">Plase input again..."
	print ">Plase input the date..."
	while 0==0:
		try:
			print ">",
			date = raw_input()
			break
		except:
			print ">Plase input again..."
	os.system("python schedule_manager.py "+date+" List"+str(num))
def print_Main():
	clear()
	print ">A.Add a list"
	print ">R.Review a list"
	print ">Q.Quit"
print_Main()
while 0==0:
	c = raw_input()
	if (c=="Q"):
		break
	else:
		if (c=="A"):
			print_add()
		else:
			if (c=="R"):
				print_review()
	print_Main()
