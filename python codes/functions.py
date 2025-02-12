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
