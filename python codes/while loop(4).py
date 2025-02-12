# Looping Statements:-
# While loop
# for loop
# WAP to print "hello world" for 5 times
i = 0
while i < 5:
    print('Hello world')
    i += 1

# WAP to print first 10 natural numbers.
i = 1
while i <= 100:
    print(i)
    i += 1

# WAP to print first n natural numbers
n = int(input('enter the number:'))
i = 1
while i <= n:
    print(i)
    i += 1

# WAP to print all the even numbers from 1 to 10.
i = 1
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1
#               or
i = 2
while i <= 10:
    print(i)
    i += 2

# WAP to print all the numbers which are divisible by 3 in between user entered limits
a = int(input('enter the starting range:'))
b = int(input('enter the ending range:'))
i = a
while i <= b:
    if i % 3 == 0:
        print(i)
    i += 1

# WAP to print the multiplication table of a user entered number.
a = int(input('enter the number:'))
i = 1
while i <= 10:
    print(f"{a} * {i} = {a * i}")
    i += 1

# WAP to check whether the entered character is uppercase alphabet or not.
a = input('enter the character:')
if 'A' <= a <= 'Z':
    print('The entered character is uppercase alphabet')
else:
    print('the entered character is lowercase alphabet')

# WAP to print all the character of a given string.
a = input('enter the string')
i = 0
while i < len(a):
    print(a[i])
    i += 1
# WAP to print all the uppercase alphabtes from the given string.
a = input('enter the String:')
i = 0
while i < len(a):
    if 'A' <= a[i] <= 'Z' or a[i] == ' ':
        print(a[i])
    i += 1

# WAP to copy all the characters form one variable to another variable.
a = input('enter the string:')
res = ''
i = 0
while i < len(a):
    res += a[i]
    i += 1
print(res)

# WAP to extract all the uppercase alphabets from the user given string.
a = input('enter the string:')
res = ''
i = 0
while i < len(a):
    if 'A' <= a[i] <= 'Z':
        res = res + a[i]
    i += 1

# WAP to seperate all the characters from the given string
a = input('enter the string:')
uc, lc, nc, sc = '', '', '', ''
i = 0
while i < len(a):
    if a[i].isupper():
        uc += a[i]
    elif a[i].islower():
        lc += a[i]
    elif a[i].isnumeric():
        nc += a[i]
    else:
        sc += a[i]
    i += 1

print(uc)
print(lc)
print(nc)
print(sc)

# WAP to reverse the given string without using any built in functions & slicing.
a = input('enter the stinring:')
res = ''
i = 0
while i < len(a):
    res = a[i] + res
    i += 1
print(res)

# WAP to check whether the given string is palindrome or not.
a = input('enter the string:')
res = ''
i = 0
while i < len(a):
    res = a[i] + res
    i += 1

if res == a:
    print('the entered strins is a palindrome')
else:
    print('the entered string is not a palindrome')

## WAP to find the number of special characters in  the given string
a = input('enter the string:')
count = 0
i = 0
while i < len(a):
    if not ('a' <= a[i] <= 'z' or 'A' <= a[i] <= 'Z' or '0' <= a[i] <= '9'):
        count += 1
    i += 1
print(count)

## WAP to find the number of words in the given string
a = input('enter the string')
res = 0
i = 0
while i < len(a):
    if ' ' == a[i]:
        res += 1
    i += 1

print(res + 1)

## WAP to check whether the string contains only uppercase alphabets or not
a = input('enter the string:')
res = 0
i = 0
while i < len(a):
    if 'A' <= a[i] <= 'Z':
        res += 1
    i += 1

if res == len(a):
    print('yes')
else:
    print('no')

# WAP to replace the space character with underscore in the given string.
a = input('enter the string:')
res = ''
i = 0
while i < len(a):
    if a[i] == ' ':
        res += '_'
    else:
        res += a[i]
    i += 1

print(res)

# WAP to toggle the given string.
a = input('eanter the string:')
res = ''
i = 0
while i < len(a):
    if 'A' <= a[i] <= 'Z':
        res += chr(ord(a[i]) + 32)
    elif 'a' <= a[i] <= 'z':
        res += chr(ord(a[i]) - 32)
    else:
        res += a[i]
    i += 1

print(res)

# WAP to Split the given string without using split function

a = input('enter the string:')
res = []
d = ''
i = 0
while i < len(a):
    if a[i] == ' ':
        res.append(d)
        d = ''
    else:
        d += a[i]
    i += 1
if d:
    res.append(d)

print(res)

a = input('enter the string:')
res = []
c = input('enter the character:')
d = ''
i = 0
while i < len(a):
    if a[i] == c:
        res.append(d)
        d = ''
    else:
        d += a[i]
    i += 1
if d:
    res.append(d)

print(res)
# WAP to remove the duplicate characters from the given string.
a = input('enter the string:')
res = ''
i = 0
while i < len(a):
    if a[i] not in res:
        res += a[i]
    i += 1
print(res)

a = input('enter the string:')
print(a)

b = int(input('enter the number'))
print(b)

c = eval(input('enter the list:'))
print(c)

# WAP to find the sum of all the numbers from the given homogeneous list
a = [10, 20, 30, 40, 50]
i = 0
res = 0
while i < len(a):
    res += a[i]
    i += 1

print(res)

# WAP to find the sum of all the numbers from the given heterogeneous list

a = ['steve', 10.9, 20, 'python', 30, [10, 22, 19], 40.6, 50]
i = 0
res = 0
while i < len(a):
    if isinstance(a[i], (int, float, complex)):
        res += a[i]
    i += 1

print(res)

a = ['steve', 10.9, 20, 'python', 30, [10, 22, 19], 40.6, 50]
i = 0
res = []
d = 0
while i < len(a):
    if isinstance(a[i], (int, float, complex)):
        d += a[i]
    else:
        res.append(a[i])
    i += 1
res.append(d)
print(res)

# WAP to extract all the integer values from the given list

a = ['steve', 10.9, 20, 'python', 30, [10, 22, 19], 40.6, 50]
res = []
i = 0
while i < len(a):
    if isinstance(a[i], int):
        res.append(a[i])
    i += 1
print(res)

# WAP to remove the duplicate elements from the given list.
a = [10.9, 20, 30, 40.6, 50]
res = []
i = 0
while i < len(a):
    if a[i] not in res:
        res.append(a[i])
    i += 1
print(res)

# WAP to find the greatest number in the given homogeneous list

a = [10, 20, 30, 40, 50]
res = 0
i = 0
while i < len(a):
    if a[i] > res:
        res = a[i]
    i += 1

# WAP to check whether the given list is homogeneous list or heterogeneous
a = [10, 20, 30, 40.9, 50]
res = []
i = 0
while i < len(a):
    if type(a[i]) not in res:
        res.append(type(a[i]))
    i += 1

if len(res) == 1:
    print('homogeneous')
else:
    print('Heterogeneous')

a = ['python', 'is', 'easy']
# o/p:- {'python': 6, 'is': 2, 'easy': 4}
res = {}
i = 0
while i < len(a):
    res[a[i]] = len(a[i])
    i += 1
print(res)

a = ['steve', 'allen', 'mark', 'miller', 'jogesh', 'lokesh', 'ramesh', 'suresh', 'mahesh']
# O/P:- {'mark': 4, 'miller': 6, 'jogesh': 6, 'lokesh': 6, 'ramesh': 6, 'suresh': 6, 'mahesh': 6}
res = {}
i = 0
while i < len(a):
    if len(a[i]) % 2 == 0:
        res[a[i]] = len(a[i])
    i += 1
print(res)

a = ['steve', 'allen', 'mark', 'miller', 'jogesh', 'lokesh', 'ramesh', 'suresh', 'mahesh']
# O/P:- {'steve': 'evets', 'allen': 'nella', 'mark': 4, 'miller': 6, 'jogesh': 6, 'lokesh': 6, 'ramesh': 6, 'suresh': 6, 'mahesh': 6}
res = {}
i = 0
while i < len(a):
    if len(a[i]) % 2 == 0:
        res[a[i]] = len(a[i])
    else:
        res[a[i]] = a[i][::-1]
    i += 1
print(res)

a = ['steve', 'allen', 'mark', 'miller', 'jogesh', 'lokesh', 'ramesh', 'suresh', 'mahesh', 'akash']

# o/p:- {'s': ['steve', 'suresh'], 'a': ['allen', 'akash'], 'm': ['miller', 'mark', 'mahesh'], 'j': ['jogesh'], 'l':['lokesh'], 'r': ['ramesh']}
res = {}
i = 0
while i < len(a):
    if a[i][0] in res:
        res[a[i][0]].append(a[i])
    else:
        res[a[i][0]] = [a[i]]
    i += 1
print(res)

# WAP to count howmany times a character is repeated in the given string
a = 'banana'
res = {}
i = 0
while i < len(a):
    if a[i] in res:
        res[a[i]] += 1
    else:
        res[a[i]] = 1
    i += 1
print(res)

res1 = {}
i = 0
while i < len(a):
    res1[a[i]] = a.count(a[i])
    i += 1
print(res1)

# WAP to get the list of the divisors of the given number
a = int(input('enter the number:'))
res = []
i = 1
while i < a:
    if a % i == 0:
        res.append(i)
    i += 1

print(res)

# WAP to check whether the entered number is prime or not
a = int(input('enter the number:'))
res = []
i = 1
while i < a:
    if a % i == 0:
        res.append(i)
    i += 1

if len(res) == 1:
    print('the given number is prime number')
else:
    print('the given number is not a prime number')

# WAP to check whether the given number is perfect or not
a = int(input('enter the number:'))
res = []
i = 1
while i < a:
    if a % i == 0:
        res.append(i)
    i += 1

print(res)
if a == sum(res):
    print('the given number is  perfect')
else:
    print('the given number is not a perfect')

a = int(input('enter the number:'))
res = 0
i = 1
while i < a:
    if a % i == 0:
        res += i
    i += 1

if res == a:
    print('the given number is  perfect')
else:
    print('the given number is not a perfect')

# WAP to check whether the give numbers are amicable or not
a = int(input('enter the number:'))
b = int(input('enter the number:'))
c, d = 0, 0
i = 1
while i < a:
    if a % i == 0:
        c += i
    i += 1

i = 1
while i < b:
    if b % i == 0:
        d += i
    i += 1

if c == b and d == a:
    print('The entered numbers are amicable numbers')
else:
    print('The entered numbers are not an amicable numbers')

# WAP to find the sum of first n natural numbers
n = int(input('enter the number:'))
res = 0
i = 1
while i <= n:
    res += i
    i += 1

print(res)

# WAP to find the factorial of a given number
n = int(input('enter the number:'))
res = 1
i = 1
while i <= n:
    res *= i
    i += 1

print(res)

# WAP to find the sum of all the individual digits of a given integer number
a = int(input('enter the number:'))
res = 0
i = a
while i > 0:
    res += i % 10
    i //= 10

print(res)

# WAP to reverse the given integer number
a = int(input('enter the number:'))
res = 0
i = a
while i > 0:
    res = (res * 10) + i % 10
    i //= 10

print(res)

# WAP to check whether the give number is armstrong or not
a = int(input('enter the number:'))
res = 0
i = a
l = len(str(a))
while i > 0:
    res += (i % 10) ** l
    i //= 10

if res == a:
    print('the given number is armstromg number')
else:
    print('the given number is not an armstrong')

# WAP to pring first n fibonacci series numbers.
n = int(input('enter the number:'))
i = 0
a = 0
b = 1
while i < n:
    print(a)
    c = a + b
    a, b = b, c
    i += 1

i = 8
c = 0
while i < 100:
    if i % 7 == 0:
        print(i)
        c += 1
    if c == 3:
        break
    i += 1

i = 0
while i < 10:
    if i % 2 == 0:
        i += 1
        continue
    else:
        print(i)
    i += 1
