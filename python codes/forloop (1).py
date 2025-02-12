# WAP to print all the characters of a string using for loop
a = 'python'
for i in a:
    print(i)


# WAP to extract all the characters from one string variable to another variable.
a = input('enter the string:')
res = ''
for i in a:
    res += i
print(res)


# WAP to check whether the entered string is palindrome or not.
a = input('enter the string:')
rev = ''
for i in a:
    rev = i + rev

if rev == a:
    print('the given string is a palindrome')
else:
    print('the given string is not a palindrome')


# WAP to separate all the type of characters of a given string
a = input('enter the string:')
uc, lc, nc, sc = '', '', '', ''
for i in a:
    if i.isupper():
        uc += i
    elif i.islower():
        lc += i
    elif i.isnumeric():
        nc += i
    else:
        sc += i

print(uc)
print(lc)
print(nc)
print(sc)

a = input('enter the string')
for i in range(len(a)):

    print(f"the index of the character :{a[i]} is :{i}")


# WAP to print the characters of the string if it is in even index position
a = input('enter the string')
for i in range(len(a)):   # for i in 0, 1, 2, 3, 4, 5
    if i % 2 == 0:
        print(f"the index of the character :{a[i]} is :{i}")

a = input('enter the string')
for i in range(0, len(a), 2):   # for i in 0, 2, 4
    print(f"the index of the character :{a[i]} is :{i}")

a = 'python'
for index, element in enumerate(a):
    if index % 2 == 0:
        print(element)

# WAP to extract all the float values from the given heterogeneous list collections
a = eval(input('enter the list collection:'))
res = []
for i in a:
    if isinstance(i, float):
        res.append(i)
print(res)

# WAP to extract all the mutable data items from the user entered list collection
a = eval(input('enter the list collection:'))
res = []
for i in a:
    if isinstance(i,(list, set, dict)):
        res.append(i)
print(res)

# WAP to find the greatest number in the given homogeneous list
a = [10, 22, 19, 57, 91, 76, 11]
g = 0
for i in a:
    if i > g:
        g = i
print(g)

# WAP to remove the duplicates from the given list
a = [10, 22, 10, 29, 38, 592, 11, 10, 22, 11]
res = []
for i in a:
    if i not in res:
        res += [i]
print(res)
# ---------------------------------or---------------------------------------
a = [10, 22, 10, 29, 38, 592, 11, 10, 22, 11]
for i in a:
    if a.count(i) >1:
        a.remove(i)
print(a)

a = ['steve', 'allen', 'mark', 'miller', 'jogesh', 'lokesh', 'ramesh', 'suresh', 'mahesh', 'akash']
# o/p:- {'s': ['steve', 'suresh'], 'a': ['allen', 'akash'], 'm': ['miller', 'mark', 'mahesh'], 'j': ['jogesh'],
# 'l':['lokesh'], 'r': ['ramesh']}
res = {}
for i in a:
    if i[0] in res:
        res[i[0]].append(i)
    else:
        res[i[0]] = [i]

print(res)
# ----------using default dictionary------------------------
from collections import defaultdict

res = defaultdict(list)
for i in a:
    res[i[0]].append(i)
print(res)
