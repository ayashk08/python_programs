### 1. WAP to check whether the entered number is possitive or not
##a = int(input('enter the number:'))
##if a > 0:
##    print('The entered number is positive number')
##
### 2. WAP to check whether the entered character is uppercase alphabet or not.
##a = input('enter the character')
##if a.isupper():
##    print('The entered character is uppercaase alphabet')
##    
### 3. WAP to check whether the entered character is numerical character  or not.
##a = input('enter the character')
##if '0' <= a <= '9':
##    print('The entered character is numerical character')
##
### 4. WAP  to check whether the entered character is special or not.
##a = input('enter the character')
##if not(a.isalnum()):
##    print('The entered chcracter is a special character')
##
### 5. WAP to check whether the entered number is even or not
##a = int(input('enter the number:'))
##if a % 2 == 0:
##    print('The entered number is even number')
##
### 6. WAP to check whether the entered number is Odd or not
##a = int(input('enter the number:'))
##if a % 2 != 0:
##    print('The entered number is Odd number')
##
### 7. WAP to check whether the entered number is divisible by 7 & 3 or not.
##a = int(input('enter the number:'))
##if a % 7 == 0 and a % 3 == 0:
##    print('The entered number is divisible by 3 & 7')
##
### 8. WAP to check whether the entered number is multiple by 4 or not.
##a = int(input('enter the nunber:'))
##if a % 4 == 0:
##    print('the entered number is multiple of 4')
##
### WAP to check whether the entered number is even number or odd number.
##a = int(input('enter the number:'))
##if a % 2 == 0:
##    print('the entered number is even number')
##else:
##    print('the entered number is odd number')
##    
### WAP to check whether the entered alphabet is uppercase alphabet or not
##a = input('enter the alphabet')
##if a.isupper():
##    print('the entered character is uppercase alphabet')
##else:
##    print('the entered character is lowercase alphabet')
##
### WAP to check whether the entered alphabet is vowel or consonent.
##a = input('enter the alphabet')
##if a in 'AEIOUaeiou':
##    print('the entered character is vowel')
##else:
##    print('The entered chcracater is consonant')
##
### WAP to find the greatest number in the given two numbers
##a = int(input('enter the number 1:'))
##b = int(input('enter the number 2:'))
##if a > b:
##    print(f'{a} is greatest')
##else:
##    print(f'{b} is greatest')
##
### WAP to check whether the entered number is divisibly by 7 and 3 or not
##a = int(input('enter the number 1:'))
##if a % 7 == 0 and a % 3 == 0:
##    print('the entered number is divisible by both 7 & 3')
##else:
##    print('the entered number is not divisible by both 7 & 3')

### 1. WAP to check whether the entered number is possitive or not
### 2. WAP to check whether the entered character is uppercase alphabet or not.
### 3. WAP to check whether the entered character is numerical character  or not.
### 4. WAP  to check whether the entered character is special or not.
##a = input('enter the character')
##if not('a'<=a<='z' or 'A'<=a<='Z' or '0'<=a<='9'):
##    print('The entered character is a special character')
##else:
##    print('The entered character is not a special character')
### 5. WAP to check whether the entered number is even or not
### 6. WAP to check whether the entered number is Odd or not
### 7. WAP to check whether the entered number is divisible by 7 & 3 or not.
### 8. WAP to check whether the entered number is multiple by 4 or not.
##
### WAP to find the relation between two numbers.
##a = int(input('enter the number 1:'))
##b = int(input('enter the number 2:'))
##if a > b:
##    print(f'a : {a} is greatest')
##elif b > a:
##    print(f'b : {b} is greatest')
##else:
##    print('Both a & b are same')
##
### WAP to find the greatest number among 3 numbers.
##a = int(input('enter the number 1:'))
##b = int(input('enter the number 2 :'))
##c = int(input('enter the number 3:'))
####if a > b and a > c:
####    print(f"a {a} is greatest number")
####elif b > a and b > c:
####    print(f"b {b} is greatest number")
####elif c > a and c > b:
####    print(f"c {c} is greatest number")
##
##if a > b and a > c:
##    print(f"a {a} is greatest number")
##elif b > c:
##    print(f"b {b} is greatest number")
##else:
##    print(f"c {c} is greatest number")
##
### WAP to find the type of the character.
##a = input('enter the character')
##if 'A'<=a<='Z':
##    print('The entered character is uppercase alphabet')
##elif 'a'<=a<='z':
##    print('the entered character is lowercase alphabet')
##elif '0'<=a<='9':
##    print('The entered character is numerical character')
##else:
##    print('The entered character is special character')
##
### WAP to check whether the entered integer number is 1 digit or 2 digit or 3 digit or 4 digit or morethan 4 digits
##a = int(input('enter the number'))
##if -9 <= a <= 9:
##    print('the entered numberis single digit')
##elif -99 <= a <= 99:
##    print('the entered number is 2 digit number')
##elif -999 <= a <= 999:
##    print('the entered number is 3 digit number')
##elif -9999 <= a <= 9999:
##    print('the entered number is 4 digit number')
##else:
##    print('the entered number is morethan 4 digit number')
##
##
### WAP to predict the result of the student by accepting his percentage.
##a = float(input('enter the  number'))
##if 90 <= a <= 100:
##    print('Distinction')
##elif 70 <= a <= 89:
##    print('First Class')
##elif 50 <= a <= 69:
##    print('Second Division')
##elif 35 <= a <= 50:
##    print('Just Pass')
##elif 0 <= a <= 35:
##    print('Betterluck Next time')
##else:
##    print('Invalid Input')
##    
##
##
##a = int(input('enter the number of units'))
##if 0 <= a <= 100:
##    print('No charges')
##elif 101 <= a <= 200:
##    print(f"the bill is {(a-100)*5}")
##elif a > 200:
##    print(f" the bill is {(a-200)*10+500}")

### WAP ro check whether the entered character is Uppercase vowel or not
##a = input('enter the character:')
##if a.isupper():
##    if a in 'AEIOU':
##        print('the entered character is uppercase vowel character')
##    else:
##        print('the entered character is uppercase but not an vowel')
##else:
##    print('The entered character is not at all uppercase alphabet')
     
### WAP to check whether the entered value is of integer or not,
### if it is integer check whether the itis divisible by 3 or not
##a = "33"
##if isinstance(a, int):
##    if a % 3 == 0:
##        print('the given value is integer and it is divisible by 3')
##    else:
##        print('the given value is integer but it is not divisible by 3')
##else:
##    print('The given value is not at all an integer')
##
### WAP to check whether the given value is mutable or not
### if it is mutable check whether the value is list or not.
##a = {10, 20, 30}
##if isinstance(a, (list, set, dict)):
##    if isinstance(a, list):
##        print('The value is list')
##    else:
##        print('the value is mutable but not a List')
##else:
##    print('the value is not a mutable')
##
# WAP to check whether the value is of a collection or not
# if it is a collection, check whether it has middle value or not,
# if it has a middle value print it
##a = 222
##if isinstance(a, (str, list, tuple, set, dict)):
##    if len(a) %2 != 0:
##        print(a[len(a)//2])
##    else:
##        print('The colection has no middle value')
##else:
##    print('The given value is not at all a collection')
##    
##
##username = 'likith_1003'
##password = '12345@Likith'
##un = input('enter the username:')
##if un == username:
##    pw = input('enter the password')
##    if pw == password:
##        print('Loggedin Successfull')
##    else:
##        print('Invalid Password')
##else:
##    print('User Not found')


# WAP to find the first greatest number among given 4 numbers.
##
##a = int(input('enter the number:'))
##b = int(input('enter the number:'))
##c = int(input('enter the number:'))
##d = int(input('enter the number:'))
##if a > b:
##    if a > c:
##        if a > d:
##            print('a is greatest')
##        else:
##            print('d is greatest')
##    else:
##        if c > d:
##            print('c is greatest')
##        else:
##            print('d is greatest')
##else:
##    if b > c:
##        if b > d:
##            print('b is greatest')
##        else:
##            print('d is greatest')
##    else:
##        if c > d:
##            print('c is greatest')
##        else:
##            print('d is greatest')


a = int(input('enter the number:'))
b = int(input('enter the number:'))
c = int(input('enter the number:'))
d = int(input('enter the number:'))
if a > b and a > c and a > d:
    if b > c and b > d:
        print('b is second greatest')
    elif c > d:
        print('c is second greatest')
    else:
        print('d is second greatest')
elif b > c and b > d:
    if a > c and a > d:
        print('a  is second greatest')
    elif c > d:
        print('c is second greatest')
    else:
        print('d is second greatest')
elif c > d:
    if a > b and a > d:
        print('a is second greatest')
    elif b > d:
        print('b is second greatest')
    else:
        print('d is second greatest')
else:
    if a > b and a > c:
        print('a is second greatest')
    elif b > c:
        print('b is second greatest')
    else:
        print('c is second greatest')











