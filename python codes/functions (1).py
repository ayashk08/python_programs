# Functions

def greet():
    print('Hello World')


def greet1():
    return "hello"


# Here name is a formal argument
def greet_someone(name):
    return f"hello {name}"


def msg(name, age, pay):
    return f"Hello {name} you are {age} years of age and you get ${pay} as a pay"


# here name is mandatary argument, age & pay are optional
def msg1(name, age=18, pay=1000):
    return f"Hello {name} you are {age} years of age and you get ${pay} as a pay"


# Here name cna be either positional or keyword argument whereas age and pay are mandetorly keyword only argument
def msg2(name, /, *, age=18, pay=1000):
    # The arguments which are at RHS of "*" will be considered as keyword only arguments
    return f"Hello {name} you are {age} years of age and you get ${pay} as a pay"


# Here age, pay can be either positional or keyword argument whereas name is mandetorly positional only argument
def msg3(name, /, age=18, pay=1000):
    # The arguments which are at LHS of "/" will be considered as positional only arguments
    return f"Hello {name} you are {age} years of age and you get ${pay} as a pay"


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def add1(a, b, c):
    return a + b + c


def add2(a, b, c, d):
    return a + b + c + d


def func(*args):
    print(args)


def add(a, b, *args):
    res = a + b
    for i in args:
        res += i
    return res


a = 10, 20, 30, 40, 50, 60
print(type(a))


def add(a, b, c, d):
    return a + b + c + d


values = (10, 20, 30, 40)


def demo(**kwargs):
    print(kwargs)


def div(n):
    res = []
    for i in range(1, n):
        if n % i == 0:
            res.append(i)
    return res


# WAP to check whether the entered number is prime number or not
def is_prime(a):
    return len(div(a)) == 1


# WAP to extract all the prime numbers oin between the user entered limits
def primes(s, e):
    res = []
    for i in range(s, e+1):
        if is_prime(i):
            res.append(i)
    return res


# WAP to check whether the entered number is perfect number or not.
def is_perfect(n):
    return sum(div(n)) == n


# WAP to extract all the perfect number in between user entered limits
def perfects(s, e):
    res = []
    for i in range(s, e+1):
        if is_perfect(i):
            res.append(i)
    return res


# WAP to check whether the entered numbers are amicable or not
def amicable(a, b):
    if sum(div(a)) == b and sum(div(b)) == a:
        print('The entered numbers are amicable numbers')
    else:
        print('the entered numbers are not an amicable numbers')