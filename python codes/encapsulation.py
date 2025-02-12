# Public Access Specifiers
class Bank:
    bname = 'SBI'
    branch = 'BBSR'
    manager = 'Smaraki'
    ceo = 'Abakash'
    cno = 1236547890
    ifsc = 'SBIN0021519'

    def __init__(self, name, pno, email, add, aadhar, pan, bal):
        self.name = name
        self.pno = pno
        self.email = email
        self.add = add
        self.aadhar = aadhar
        self.pan = pan
        self.bal = bal
        self.transactions = []

    def deposit(self, amount):
        if amount >= 50000:
            upan = input('enter the User Pan number:')
            if upan == self.pan:
                self.bal += amount
                self.transactions.append(f"Credited amount of {amount}")
            else:
                print('PAN Number is not matching ')
        else:
            self.bal += amount
            self.transactions.append(f"Credited amount of {amount}")

    def withdraw(self, amount):
        if self.bal >= amount:
            self.bal -= amount
            self.transactions.append(f"Debited amount of {amount}")
        else:
            print('Insufficient Balance')

    def display(self):
        for member, value in self.__dict__.items():
            print(f"The {member} of the customer is {value}")

    def statement(self):
        for transaction in self.transactions:
            print(transaction)
        print(f"The Available Balance is {self.bal}")


c1 = Bank('steve', 852741586913, 'steve@gmail.com', 'BBSR',
          225588774411, 'abcd1234x', 5000)


# Protected Access Specifiers
class Bank2:
    bname = 'SBI'
    branch = 'BBSR'
    manager = 'Smaraki'
    ceo = 'Abakash'
    cno = 1236547890
    ifsc = 'SBIN0021519'

    def __init__(self, name, pno, email, add, aadhar, pan, bal):
        self._name = name
        self._pno = pno
        self._email = email
        self._add = add
        self._aadhar = aadhar
        self._pan = pan
        self._bal = bal
        self._transactions = []

    def deposit(self, amount):
        if amount >= 50000:
            upan = input('enter the User Pan number:')
            if upan == self._pan:
                self._bal += amount
                self._transactions.append(f"Credited amount of {amount}")
            else:
                print('PAN Number is not matching ')
        else:
            self._bal += amount
            self._transactions.append(f"Credited amount of {amount}")

    def withdraw(self, amount):
        if self._bal >= amount:
            self._bal -= amount
            self._transactions.append(f"Debited amount of {amount}")
        else:
            print('Insufficient Balance')

    def display(self):
        for member, value in self.__dict__.items():
            print(f"The {member} of the customer is {value}")

    def statement(self):
        for transaction in self._transactions:
            print(transaction)
        print(f"The Available Balance is {self._bal}")


c2 = Bank2('Allen', 8855229966, 'allen@gmail.com', 'Pune', 445566332211, 'xyza1254x', 5000)
# Protected Access Specifiers


class Bank3:
    bname = 'SBI'
    branch = 'BBSR'
    manager = 'Smaraki'
    ceo = 'Abakash'
    cno = 1236547890
    ifsc = 'SBIN0021519'

    def __init__(self, name, pno, email, add, aadhar, pan, bal):
        self.__name = name
        self.__pno = pno
        self.__email = email
        self.__add = add
        self.__aadhar = aadhar
        self.__pan = pan
        self.__bal = bal
        self.__transactions = []

    def deposit(self, amount):
        if amount >= 50000:
            upan = input('enter the User Pan number:')
            if upan == self.__pan:
                self.__bal += amount
                self.__transactions.append(f"Credited amount of {amount}")
                self.__msg()
            else:
                print('PAN Number is not matching ')
        else:
            self.__bal += amount
            self.__transactions.append(f"Credited amount of {amount}")
            self.__msg()

    def withdraw(self, amount):
        if self.__bal >= amount:
            self.__bal -= amount
            self.__transactions.append(f"Debited amount of {amount}")
            self.__msg()
        else:
            print('Insufficient Balance')

    def display(self):
        for member, value in self.__dict__.items():
            print(f"The {member} of the customer is {value}")

    def statement(self):
        for transaction in self.__transactions:
            print(transaction)
        print(f"The Available Balance is {self.__bal}")

    @staticmethod
    def __msg():
        print('Transaction Successful')


c3 = Bank3('likith', 8179267926, 'likith@gmail.com', 'Lepakshi', 885522001144, 'poiu5247x', 257821)