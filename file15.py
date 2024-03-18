# from tkinter import *
# import webbrowser
# a=Tk()
# a.title('GUI')
# a.geometry('500x500')
# def info():
#     webbrowser.open('https://www.google.com/')
# Button(a,text='Open',command=info).pack()
import mysql.connector
a= mysql.connector.connect(host='localhost',user='root',password='shubh@1234')
b=a.cursor()
c='create databases registration'
b.execute(c)
