# 1. WAP to check whether the entered number is possitive or not
a = int(input('enter the number:'))
if a > 0:
    print('The entered number is positive number')

# 2. WAP to check whether the entered character is uppercase alphabet or not.
a = input('enter the character')
if a.isupper():
    print('The entered character is uppercaase alphabet')
    
# 3. WAP to check whether the entered character is numerical character  or not.
a = input('enter the character')
if '0' <= a <= '9':
    print('The entered character is numerical character')

# 4. WAP  to check whether the entered character is special or not.
a = input('enter the character')
if not(a.isalnum()):
    print('The entered chcracter is a special character')

# 5. WAP to check whether the entered number is even or not
a = int(input('enter the number:'))
if a % 2 == 0:
    print('The entered number is even number')

# 6. WAP to check whether the entered number is Odd or not
a = int(input('enter the number:'))
if a % 2 != 0:
    print('The entered number is Odd number')

# 7. WAP to check whether the entered number is divisible by 7 & 3 or not.
a = int(input('enter the number:'))
if a % 7 == 0 and a % 3 == 0:
    print('The entered number is divisible by 3 & 7')

# 8. WAP to check whether the entered number is multiple by 4 or not.
a = int(input('enter the nunber:'))
if a % 4 == 0:
    print('the entered number is multiple of 4')


