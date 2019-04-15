from tkinter import *
import os
import time
from tkinter import messagebox


def read_defult_values():
	CONFIGFILE = "config.txt"
	f_openconfigfile = open(CONFIGFILE)
	configurations = f_openconfigfile.readlines()
	f_openconfigfile.close()
	values = []
	parameters= []
	for each in range(len(configurations)):
		if "=" in configurations[each]:
			values.append (configurations[each].split("=")[1].replace("\n",""))
			parameters.append (configurations[each].split("=")[0].replace("\n",""))
	label_list=[]
	for each1 in range(len(parameters)):
		l=Label(frame, text=str(parameters[each1]),borderwidth=1,bg="black", fg="white")
		e=Entry(frame, bd =5,width = 100)
		label_list.append(l)
		entry_list.append(e)
		l.grid(row=each1,column=0,sticky=W)
		e.grid(row=each1,column=1,sticky=W,columnspan=3)
		e.insert(100,str(values[each1]))
	print(str(len(entry_list)))
	
def replace_config():
	CONFIGFILE = "runtime_config.txt"
	f_openconfigfile = open("config.txt")
	configurations= f_openconfigfile.readlines()
	f_openconfigfile.close()
	f_openconfigfile = open(CONFIGFILE,"w")
	parameters= []
	for each in range(len(configurations)):
		if "=" in configurations[each]:
			parameters.append (configurations[each].split("=")[0].replace("\n","")+"=")
	for each in range(len(parameters)):
		print(str(entry_list[each].get()))
		parameters[each]= str(parameters[each])+str(entry_list[each].get())		
	for each in range(len(parameters)):		
		f_openconfigfile.write(parameters[each]+"\n")
	f_openconfigfile.close()
entry_list=[]

def readfile():
	start_line=0
	isautomation = True
	while (isautomation):
		last_line = return_lastline()
		buffer = []
		if (start_line == last_line):
			isautomation = False
			print("EOF, Logging completed")
			break;
		else:
			f_open = open("log.txt")
			f_lines = f_open.readlines()
			f_open.close()
			for each in range (start_line,last_line):
				buffer.append(str(f_lines[each]).replace("{","").replace("}",""))
				T.insert(END,buffer)
			start_line=last_line
			time.sleep(10)
	
def return_lastline():
	f_open = open("log.txt")
	f_lines = f_open.readlines()
	f_open.close()
	last_line = len(f_lines)
	return last_line
			
	
def start_automation():
	os.system(str(entry_list[0].get())+"\\Start_Automation.bat")
	print("Triggered Automation")
	time.sleep(15)
	readfile()
	
def stop_automation():
	os.system(str(entry_list[0].get())+"\\Stop_Automation.bat")
	print("Stopped Automation")	

def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=500,height=300,bg="white")

root=Tk()
sizex = 1000
sizey = 1000
posx  = 100
posy  = 100
root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

myframe=Frame(root,relief=GROOVE,width=50,height=100,bd=1)
myframe.place(x=10,y=50)

myframe1=Frame(root,relief=GROOVE,width=50,height=50,bd=1)
myframe1.place(x=10,y=400)

myframetitle=Frame(root,relief=GROOVE,width=15,height=1,bd=4)
myframetitle.place(x=50,y=0)

canvas=Canvas(myframe)
frame=Frame(canvas)
myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)
myscrollbar.pack(side="right",fill="y")
canvas.pack(side="left")
canvas.create_window((0,0),window=frame,anchor='nw')
frame.bind("<Configure>",myfunction)

S = Scrollbar(myframe1)
T = Text(myframe1, height=20, width=100)
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)

Title = Text(myframetitle, height=1, width=15, bd=4, bg="black", fg="white")
Title.insert(END,"CONFIGURATIONS")
Title.pack(side=TOP,fill=Y)
Title.config(state=DISABLED)


read_defult_values()
write_frame = Frame(root,height=100,width=100)
write_frame.place(x=600,y=20)
B = Button(write_frame , text ="Save config", command = replace_config).grid(row=0,column=2)
B1 = Button(write_frame , text ="Start Automation", command = start_automation,activebackground="navy",activeforeground="red").grid(row=1,column=2)
B2 = Button(write_frame , text ="Stop Automation", command = stop_automation).grid(row=2,column=2)

root.mainloop()
