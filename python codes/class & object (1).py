# class DemoClass:
#     a = 10
#     b = 20
#     c = 30
#
#
# DemoObject = DemoClass()
# o1 = DemoClass()
#
#
# # Creating a class called Bank with some class members
# class Bank:
#     bname = 'SBI'
#     ceo = 'Munna'
#     mbl = 'Mumbai, Andheri'
#     manager = 'Pinki'
#     contactno = 8979759489
#     ifsc = 'SBIN0021519'
#
#
# # creating an object for a Bank Class
# c1 = Bank()
# c2 = Bank()
# c3 = Bank()
# c4 = Bank()
#
# # Initialising the members of Bank Objects(c1, c2)
# c1.name = 'likith'
# c1.pno = 8179267926
# c1.email = 'likith.d@qspiders.in'
# c1.add = 'Lepakshi'
# c1.bal = 5000
#
# c2.name = 'steve'
# c2.pno = 9585741236
# c2.email = 'steve@gmail.com'
# c2.add = 'Pune'
# c2.bal = 2980
#
#
# # creating a function Externally to initialise the members of an object
# def initialise(self, name, pno, email, add, bal):
#     self.name = name
#     self.pno = pno
#     self.email = email
#     self.add = add
#     self.bal = bal
#
#
# initialise(c3, 'sumati', 9143143598, 'sumati@gmail.com', 'sambala', '250units')
# initialise(c4, 'kyra', 85749632150, 'kyra@gmail.com', 'sambala', '1950units')
#
#
# class Bank:
#     bname = 'SBI'
#     ceo = 'Munna'
#     mbl = 'Mumbai, Andheri'
#     manager = 'Pinki'
#     contactno = 8979759489
#     ifsc = 'SBIN0021519'
#
#     def __init__(self, name, pno, email, add, bal):
#         self.name = name
#         self.pno = pno
#         self.email = email
#         self.add = add
#         self.bal = bal
#
#
# c1 = Bank('likith', 2587459615, 'likith@gmail.com', 'lepakshi', 5000)
# c2 = Bank('steve', 8559667441, 'steve@gmail.com', 'BBSR', 2546)

# class Bank:
#     bname = 'ICICI'
#     manager = 'steve'
#     ceo = 'Mark'
#     cno = 9874563210
#
#     def __init__(self, name, pno, email, add, bal):
#         self.name = name
#         self.pno = pno
#         self.email = email
#         self.add = add
#         self.bal = bal
#
#     def deposit(self, amount):
#         self.bal += amount
#         self.msg()
#
#     def withdraw(self, amount):
#         self.bal -= amount
#         self.msg()
#
#     @classmethod
#     def ch_bname(cls, new):
#         cls.bname = new
#         cls.msg()
#
#     @classmethod
#     def ch_ceo(cls, new):
#         cls.ceo = new
#         cls.msg()
#
#     @staticmethod
#     def msg():
#         print('Transaction Successful')
#
#
# c1 = Bank('Likith', 8179267926, 'likith.qsp@gmail.com', 'Lepakshi', 500000)
# c2 = Bank('Steve', 8529637410, 'steve@gmail.com', 'BBSR', 5214)
#
#
