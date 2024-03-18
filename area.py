# import socket
# a = socket.socket()
# a.bind(('localhost',1234))
# a.listen()
# msg, addr= a.accept()
# b= msg.recv(1024)
# c = b.decode()
# print(c)
#-----------------------------------------------------------------------------------------------------------------
# import turtle
# import numpy
# poly= turtle.Turtle()
# num_sides=int(input('Enter a number for sides'))
# side_length=int(input('Enter a number for sides of lenght....'))
# angle=360.0/num_sides
# for i in range(num_sides):
#     poly.forward(side_length)
#     poly.right(angle)
# turtle.done()
# import turtle
# tu=turtle.Screen()
# tu.bgcolor("light green")
# tu.title("Turtle")
# skk = turtle.Turtle()
# skk.color("blue")
# def fun1(size):
#     for i in range(4):
#         skk.forward(size)
#         skk.left(90)
#         size = size-5
# fun1(146)
# fun1(144)
# fun1(140)
# fun1(130)
# fun1(120)
# fun1(110)
# fun1(100)
# fun1(90)
# fun1(70)
# fun1(60)
# fun1(50)
# fun1(40)
# fun1(30)
# turtle.done()
#import turtle
# tu1=turtle.Screen()
# tu1.bgcolor("light blue")
# tu1.title("Turtle")
# skk1 = turtle.Turtle()
# skk1.color("red")
# def fun2(size):
#     for i in range(4):
#         skk1.forward(size)
#         skk1.left(70)
#         skk1.right(5)
#         skk1.forward(10)
#         size = size-5
# fun2(146)
# fun2(144)
# fun2(140)
# fun2(130)
# fun2(120)
# fun2(110)
# fun2(100)
# fun2(90)
# fun2(70)
# fun2(60)
# fun2(50)
# fun2(40)
# fun2(30)
# turtle.done()
# import turtle
# import turtle
# import time
# import random
# print("This program draws shapes based on the number you are enter in a uniform pattern.")
# num_str=input("Enter the side number of the shape you want to draw:...")
# if num_str.isdigit():
#     squares = int(num_str)
# angle = 180-180*(squares-2)/squares
# turtle.up
# x= 0
# y = 0
# turtle.setpos(x,y)
# numshapes = 8
# for x in range(squares):
#     turtle.begin_fill()
#     turtle.down()
#     turtle.forward(40)
#     turtle.left(angle)
#     turtle.forward(40)
#     print(turtle.pos())
#     turtle.up()
#     turtle.end_fill()
# time.sleep(20)
# turtle.isvisible()
# import turtle
# import time
# colors =['red','light green','blue']
# loadwindow = turtle.Screen()
# t=turtle.Pen()
# turtle.speed(12)
# turtle.color('orange')
# for i in range(100):
#     turtle.circle(5*i/2)
#     turtle.circle(-5*i)
#     turtle.left(i)
# turtle.exitonclick()
# import turtle
# import time
# colors = ['red','green','purple','orange','yellow','blue']
# t= turtle.Pen()
# turtle.bgcolor('black')
# t.speed(500)
# for x in range(360):
#     t.pencolor(colors[x%5])
#     t.pencolor(colors[x%5+1])
#     t.width(x//100+1)
#     t.forward(x)
#     t.left(59)
# turtle.done()
import socket
a=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
a.bind(('localhost',123))
while True:
    a1=a.recvfrom(1024)
    m=a1[0].decode()
    a2='Message form client'+m[len(m)-1]+":"+m[0:len(m)-1]
    print(a2)
    a3=a1[1]
    print(a3)
    a4=input('enter your message for client'+m[len(m)-1]+":")
    a5 =str.encode(a4)
    a.sendto(a5,a3)
