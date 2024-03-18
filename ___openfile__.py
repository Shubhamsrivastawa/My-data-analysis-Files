# import turtle
#
# t = turtle.Turtle()
#
# # radius for smallest circle
# r = 10
# turtle.back(100)
# turtle.right(1)
# # number of circles
# n = 10
# r1 = 10
# # loop for printing tangent circles
# for i in range(1, n + 1, 1):
#     t.circle(r * i)
# for j in range(1,n,2):
#     t.circle(r1*j)
#------------------------------------------------------------------------------
# import requests
# from bs4 import BeautifulSoup
# # import html5lib
# # a ='https://www.wordpress.com'
# # b =requests.get(a)
# # c =BeautifulSoup(b.content,'')
# # print(c.prettify())
# # import socket
# a = socket.socket()
# a.connect(('localhost',1234))
# m= 'hello'
# a.send(m.encode())
# a.close()
#-----------------------------------------------------------------------------------------------------------------------
# import tkinter
# a = tkinter.Tk()
# a.geometry('500x500')
# a.config(bg='light green')
# a.title('Calculator')
# def add():
#     a2=10+8
#     print(a2)
# a1=tkinter.Button(a,text='add',bg='pink',fg='red',command=add)
# a1.pack()
# a.mainloop()
# import tkinter
# a = tkinter.Tk()
# a.geometry('500x500')
# a.config(bg='light green')
# a.title('Calculator')
# def add():
#     a2=10+8
#     print(a2)
# a1=tkinter.Button(a,text='add',bg='pink',fg='red',command=add)
# a1.grid(row=0,column=0)
# a12=tkinter.Button(a,text='multi3',bg='pink',fg='red',command=add)
# a12.place(x=150,y=150)
# a13=tkinter.Button(a,text='multi2',bg='pink',fg='red',command=add,width=10,height=2)
# a13.place(x=15,y=120)
# a14=tkinter.Button(a,text='multi1',bg='pink',fg='red',command=add,width=10,height=2,font=('caalibri',14,'bold'))
# a14.place(x=60,y=60)
# a.mainloop()
# import tkinter
# a = tkinter.Tk()
# a.geometry('500x500')
# a.config(bg='light green')
# a.title('Calculator')
# a1=tkinter.Label(a,text='Enter your name')
# a1.place(x=10,y=10)
# b=tkinter.Entry(a)
# b.place(x=120,y=10)
# a2=tkinter.Label(a,text='Enter your name')
# a2.place(x=10,y=40)
# b1=tkinter.Entry(a)
# b1.place(x=150,y=40)
# a.mainloop()
# import tkinter
# import random
# a = tkinter.Tk()
# a.geometry('500x500')
# a.config(bg='light green')
# a.title('Calculator')
# b1=tkinter.Label(a,text='enter your reviews')
# b1.place(x=0,y=0)
# b=tkinter.Text(a,height=10,width=30,borderwidth=10)
# b.pack()
# a.mainloop()
import tkinter
a=tkinter.Tk()
a.geometry('500x600')
a.config(bg='light green')
a.title('Calculator')
a1=tkinter.Label(a,text='Enter your name',width='20',height='1')
a1.place(x=0,y=0)
b=tkinter.Entry(a,width=30,insertbackground='red')
b.place(x=130,y=140)
b.pack()
a2=tkinter.Label(a,text='Enter your password',width='20',height='1')
a2.place(x=0,y=30)
b2=tkinter.Entry(a,show='*',width=30,highlightbackground='red')
b2.place(x=160,y=30)
a.mainloop()
