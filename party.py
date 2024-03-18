# n=int(input('enter your number.....'))
# for i in range(1,n):       1,2,3,4,5,6,7
#     print('',end='')
#     for j in range(0,n-i): 7,6,5,4,3,2,1 (1)
#         print('*',end='')  6,5,4,3,2,1   (2)
#     print()                5,4,3,2,1     (3)
#                            4,3,2,1       (4)
#                            3,2,1         (5)
#                            2,1           (6)
#                            1             (7)
#----------------------------------------------------------------------------
# for i in range(1,6):
#     print('',end='')
#     for j in range(1,i+1):
#         print(j,end='')
#     print()
# for i in range(10,310,10):
#     print(i,end=', ')
# for i in range(105,0,-7):
#     print(i,end='
# n = input('enter any number:.....')
# b=len(n)
# c ={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
# for i in range(b):
#     d=c[int(n[i])]
#     print(d,end=' ')
# n= int(input('enter any number......'))
# for i in range(1,n):
#     print('2'*i,end=', ')
#----------------------------------------Dimond----------
# n = int(input('enter a number....'))
# for i in range(1,n):
#     for j in range(1,n-i):
#         print('',end=' ')
#     for k in range(0,i):
#         print('*',end=' ')
#     print()
# for i in range(1, n):
#     for j in range(0,i):
#         print('',end=' ')
#     for k in range(1,n-i):
#         print('*',end=' ')
#     print()
#----------Prigm----------
# n=int(input('enter a number.....'))
# for i in range(0,n):
#     for j in range(0,n-i):
#         print('*',end=' ')
#     for k in range(1,n-j):
#         print('__',end=' ')
#     for l in range(0,n-i):
#         print('*',end=' ')
#     print()\\
# n=int(input('enter any number....'))
# for i in range(0,n):
#     for j in range(0,n):
#         if i+j==n//2 or i-j==n//2 or j-i==n//2 or i+j==n//2*3:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# n= int(input('enter a number,....'))
# for num in range(n)
#     sqr = num * num
import socket
a2=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
while True:
    m=input('enter your message:')
    a=str.encode(m+'2')
    a1=('localhost',123)
    a2.sendto(a,a1)
    a3=a2.recvfrom(1024)
    a4='Message form server: '+a3[0].decode()
    print(a4)

