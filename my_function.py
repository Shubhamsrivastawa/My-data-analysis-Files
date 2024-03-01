# def maximum(a,b,c):
#     d = a+b+c//2
#     print(d)
# a1= int(input('enter a number....'))
# b1= int(input('enter a number....'))
# c1= int(input('enter a number....'))
# maximum(a1,b1,c1)
# # class cat:
#     def __init__(self,name,color,work):
#         self.name= name
#         self.color= color
#         self.work= work
#     def info(self):
#         print(self.work)
#         print(self.name)
#         print(self.color)
# a=cat('pushi','grey','eating')
# a.info()
# class cat:
#     def __init__(self,name,color,work):
#         self.name= name
#         self.color= color
#         self.work= work
#     def info(self):
#         print(self.work)
#         print(self.name)
#         print(self.color)
# a=cat('pushi','grey','eating')
# a.info()
# class cat:
#     def __init__(self,name,color,work):
#         self.name= name
#         self.color= color
#         self.work= work
#     def info(self):
#         print(self.name)
#         print(self.color)
#         print(self.work)
# a=cat('Pushi','Grey','Eating..meat')
# a.info()
# class animals:
#     def __init_(self):
#         self.name= name
#         self.color= color
#         self.work= work
#     def cat(self):
#         print(self.name)
#         print(self.color)
#         print(self.work)
# a=dog('Jackey','Black','Eating...Bread')
# a.info()
# class employee:
#     def info(self,name,salary):
#         self.name=name
#         self.salary= salary
#         print(self.name)
#         print(self.salary)
# class company(employee):
#     def info1(self,name,salary,address,position,company_add):
#         self.address = address
#         self.position = position
#         self.company_add= company_add
#         employee.info(self, name, salary)
#         print(self.address)
#         print(self.position)
#         print(self.company_add)
# a=company()
# a.info1('hind','3242','assitant','hellp','djfh')
# --------------------------------------------------------------------------------------
# multipel inherisment-------\\\
# class employee:
#     def info(self,name,salary):
#         self.name=name
#         self.salary= salary
#         print(self.name)
#         print(self.salary)
# class abc:
#     def info2(self,good):
#         self.good=good
#         print(self.good)
# class company(employee,abc):
#     def info1(self,name,salary,address,position,company_add):
#         self.address = address
#         self.position = position
#         self.company_add= company_add
#         employee.info(self, name, salary)
#         abc.info2(self,good='multile')
#         print(self.address)
#         print(self.position)
#         print(self.company_add)
# a=company()
# a.info1('hind','3242','assitant','hellp','djfh')
# ----------------------------------------------------------------------
# multilevel class-----------
# class employee:
#     def info(self,name,salary):
#         self.name=name
#         self.salary= salary
#         print(self.name)
#         print(self.salary)
# class abc(employee):
#     def info2(self,good):
#         self.good=good
#         print(self.good)
# class company(abc):
#     def info1(self,name,salary,address,position,company_add):
#         self.address = address
#         self.position = position
#         self.company_add= company_add
#         employee.info(self, name, salary)
#         abc.info2(self,good='multile')
#         print(self.address)
#         print(self.position)
#         print(self.company_add)
# a=company()
# a.info1('hind','3242','assitant','hellp','djfh')
# ----------------------------------------------------------------------------------
# class cat:
#     def info(self,name,color):
#         self.name=name
#         self.color=color
#         print('The cat is:',self.name)
#         print('The cat  color is:',self.color)
# class dog(cat):
#     def info(self,name,color,work):
#         super().info('abc','black')
#         self.name=name
#         self.color=color
#         self.work=work
#         print('The dog color is:',self.color)
#         print('The dog name is:',self.name)
#         print('The dog work is:',self.work)
# class fish(dog):
#     def info(self,name,color):
#         super().info('Rocky','Red','Sleep')
#         self.name=name
#         self.color=color
#         print('This fish name is:',self.name)
#         print('This fish color is:',self.color)
# a=fish()
# a.info('seet','golden')
#---------------------------------------------------------------------------------------------------
# class login:
#     def __info(self,username,password):
#         self.username=username
#         self.password=password
#         print(self.password)
#         print(self.username)
# a=login()
# a.__info('Shubh','shubh157')
# class registration:
#     def __info(self,username,password,mail_id):
#         self.username=username
#         self.__password=password
#         self.mail_id=mail_id
#         print(self.username)
#         print(self.password)
#         print(self.mail_id)
# a= input('Type here user name: ')
# b=input('Type here password: ')
# c=input('Type here mail_id: ')
# a1=registration()
# a1.info(a,b,c)
