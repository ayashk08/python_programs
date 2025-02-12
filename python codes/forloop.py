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
