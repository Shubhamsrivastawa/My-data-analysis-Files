'''The while keyword constructs a conditional loop.Python interpreter evaluates boolean expression and keeps on executing
the subsequent uniformly indented block of statements as long as it holds true.The moment it is no longer true,the repetition
stops and program flow proceeds to next statement in the script.A syntactical representation of usage of while loop is as
follows'''
# count = 0
# while count<5:
#     count = count+1
#     print('this is count of number',count)
# print('End of 5 repetitions')
'''Following code generates the list of numbers in Fibonacci series.First two numbers in the list are 0 and 1.Each subsequent number
is the sum of previous two numbers.The while loop in the code adds next 10 numbers.
The iterations are counted with the help of variable 'i', sum of numbers at ith and (i+1)th position is appended to the list till 'i'
#  reaches 10.'''
# n =int(input('Enter any number:........'))
# # for i in range(1,n):
#     print(' ',end=' ')
#     for j in range(1,n-i):
#         print(j,end=" ")
#         j+=1
#     for k in range(0,i-j):
#         print('_',end=" ")
#         k+=1
#     print()
#     i+=1
# f=1
# for i in range(1,n+1):
#     f = f*i
#     print('factorial of {}= {}'.format(n,f)
# numbers = [4,7,8,9,5]
# for i in range(len(numbers)):
#     sqr=numbers[i]*numbers[i]
#     print('Sqaure of {} is {}'.format(numbers[i],sqr))
#     for j in range(len(numbers)):
#         print('*',end=' ')
#         j+=1
#     print()
# dict1={'Maharashtra':'Bombay','Andhra Pradesh':'Hyderabad','UP':'Lucknow','MP':'Bhopal'}
# dict1.update({'hello':'shubham'})
# print(dict1.get('MP'))
# for pair in dict1.items():
#     print(pair)
# '''List Comprehension
# Python supports many functional programming features.List comprehension is one of them.This technique follows mathmatical
# set builder notation.It is a very concise and efficent way of creating new list by performing a certain process on each
# item of existing list. List comprehension efficient than processing a list by for loop.'''
# list1= [4,7,8,9,5,6]
# # dict1=[{num:num*num} for num in list1]
# # print(dict1)
# list.sort()
# import turtle
# import turtle
# import time
# colors =['red','blue']
# loadwindow = turtle.Screen()
# t=turtle.Pen()
# turtle.speed(1)
# for i in range(10):
#     turtle.circle(5*i)
#     turtle.left(i)
# turtle.end_fill()
# import socket
# a2=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
# while True:
#     m=input('enter your message:')
#     a=str.encode(m+'1')
#     a1=('localhost',123)
#     a2.sendto(a,a1)
#     a3=a2.recvfrom(1024)
