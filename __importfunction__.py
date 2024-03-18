#date & time modules:---------------------------
# import datetime as dt
# from datetime import *
# a = dt.datetime.fromtimestamp(356)
# print(a)
# a= dt.date.today()
# b =a.isoformat()
# print(a)
# d= a.year
# c=a.month
# print(c,d)
# print(type(b))
# import time
# a=time.localtime(time.time())
# print(a)
# import calendar
# a = calendar.weekday(2021,2,5)
# print(a)
# import calendar------------------------------------------------
# year =2022
# month=1
# i=1
# while i<=12:
#     b=calendar.calendar(2012)
#     print(b)
#     break
#     i+=1
# from tkinter import *
# from tkinter import messagebox
# from tkinter import filedialog as fd
# a=tkinter.Tk()
# a.title('gui')
# a.geometry('400x400')
# b=Spinbox(a,from_=1,to=12,borderwidth=8,width=6,bg='pink',fg='blue')
# b.place(x=40,y=50)
# a.mainloop()
# b=Scale(a,from_=1,to=50,orient=HORIZONTAL,length=200)
# b.place(x=0,y=50)
# b=Message(a,text='this is a gui')
# b.pack()
# b=Menu(a)
# a.config(menu=b)
# def info():
#     fd.askopenfile()
# def info1():
#     fd.asksaveasfilename()
# a1=Menu(b)
# b.add_cascade(label='File',menu=a1)
# a1.add_command(label='Open file')
# a1.add_command(label='save as')
# a1.add_separator()
# a1.add_command(label='Exit')
# a2=Menu(a1)
# a1.add_cascade(label='open recent',menu=a2)
# a2.add_command(label='Open new file')
# a2.add_command(label='Save file')
# a3=Menu(b)
# b.add_cascade(label='Help',menu=a3)
# b=Scrollbar(a )
# b.pack(side=RIGHT,fill=Y)
# c=Listbox(a,yscrollcommand=b.set)
# for i in range(60):
#     c.insert(END,'This is a file')
# c.pack(side=RIGHT,fill=BOTH)
# b.config(command=c.yview)
# def info():
#     if b.get()=='shubham':
#         a1=tkinter.Toplevel(a)
#         a1.title('correct info')
#         a1.geometry('300x300')
#         tkinter.Message(a1,text='Correct information').pack()
#     else:
#         messagebox.askquestion('Error','Incorrect username or password')
# b=tkinter.Entry(a)
# b.pack()
# tkinter.Button(a,text='Submit',command=info).pack()
# a.mainloop()
# a= PanedWindow()
# a.pack(fill=BOTH,expand=1)
# b=Entry(a,bd=4)
# a.add(b)
# c=Spinbox(a,from_=1,to=20)
# a.add(c)
# a=Tk()
# a.title('Gui')
# a.geometry('400x400')
# b=Listbox(height=20)
# b.insert(1,'Python')
# b.insert(2,'Java')
# b.insert((3,'c++'))
# b.pack(side=LEFT)
# a.mainloop()
# from tkinter import *
# a=Tk()
# a.title('GUI')
# a.geometry('400x400')
# b=Canvas(a,width=140,height=160,bg='red')
# b.pack()
# b.create_rectangle(10,50,50,10)
# a.mainloop()
# b=LabelFrame(a,text='This is a frame')
# b.pack(fill='both',expand='yes')
# b1=Label(b,text='this is done')
# b1.pack()
# b2=Entry(b)
# b2.pack()
# a.mainloop()
# import mysql.connector
# a= mysql.connector.connect(host='localhost',user='root',password='shubh@1234')
# b=a.cursor()
# c='create databases registration'
# b.execute(c)