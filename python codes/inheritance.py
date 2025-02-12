# Single level Inheritance
# Parent class
class Bank1:
    bname = 'SBI'
    branch = 'Nayapalli'
    manager = 'biswanath'

    # Parent class constructor
    def __init__(self, name, add, bal):
        self.name = name
        self.add = add
        self.bal = bal

    def deposit(self, amount):
        self.bal += amount

    def withdraw(self, amount):
        if self.bal >= amount:
            self.bal -= amount
        else:
            print('Insufficient Balance')

    # parent class method
    def display(self):
        print(f"The name of the customer is {self.name}")
        print(f"The Address of the customer is {self.add}")
        print(f"The Balance of the customer is {self.bal}")


c1 = Bank1('likith', 'Lepakshi', 5000)


# Child Class
class Bank2(Bank1):

    # Child Class Constructor
    def __init__(self, name, add, bal, pno, email, aadhar, pan):
        # Calling parent class constructor inside the child class constructor
        Bank1.__init__(self, name, add, bal)
        self.pno = pno
        self.email = email
        self.aadhar = aadhar
        self.pan = pan

    # chile class method
    def display(self):
        # calling parent class method inside the child class
        Bank1.display(self)
        print(f"The PNO of the customer is {self.pno}")
        print(f"The Email of the customer is {self.email}")
        print(f"The Aadhar of the customer is {self.aadhar}")
        print(f"The PAN of the customer is {self.pan}")


c2 = Bank2('steve', 'BBSR', 5000, 8529637410, 'steve@gmail.com', 885599667744, 'abcd1234x')

# Multi-level Inheritance.


class Resume1:
    def __init__(self, name, pno, email, add, tyop, tp):
        self.name = name
        self.pno = pno
        self.add = add
        self.email = email
        self.tyop = tyop
        self.tp = tp

    def ch_pno(self, new):
        self.pno = new

    def ch_email(self, new):
        self.email = new

    def ch_name(self, new):
        self.name = new

    def display(self):
        d = self.__dict__
        for member, value in d.items():
            print(f"The {member} of the candidate is {value}")


c1 = Resume1('Likith', 8179267926, 'likith@gmail.com', 'Lepakshi', 2010, 95)


class Resume2(Resume1):
    def __init__(self, name, pno, email, add, tyop, tp, twyop, twp):
        super().__init__(name, pno, email, add, tyop, tp)
        self.twyop = twyop
        self.twp = twp


c2 = Resume2('steve', 8529637410, 'steve@gmail.com', 'BBSR', 2012, 85, 2014, 84)


class Resume3(Resume2):
    def __init__(self, name, pno, email, add, tyop, tp, twyop, twp, dyop, dp):
        super(Resume3, self).__init__(name, pno, email, add, tyop, tp, twyop, twp)
        self.dyop = dyop
        self.dp = dp


c3 = Resume3('allen', 7418529630, 'allen@gmail.com', 'Chennai', 2014, 82, 2016, 88, 2019, 88)

# Multiple Inheritance


class Add:
    @staticmethod
    def add(a, b):
        return a + b


class Sub:
    @staticmethod
    def sub(a, b):
        return a - b


class Div:
    @staticmethod
    def div(a, b):
        return a / b


class Mul:
    @staticmethod
    def mul(a, b):
        return a * b


class Calc(Add, Sub, Mul, Div):
    pass


o1 = Calc()

# Hierarchical Inheritance
