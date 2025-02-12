# # 1. WAP to get the respective  o/p
# # a = 'aabcaabbccabc'
# # o/p:- 'a5b4c4'
# a = input('enter the string:')
# res = ''
# for i in a:
#     if i not in res:
#         res += i+str(a.count(i))
# print(res)

# # WAP to extract all the prime numbers in between user entered limits
# a = int(input('enter the start limit:'))
# b = int(input('enter the end limit:'))
# p = []
# for i in range(a, b+1):
#     res = []
#     for j in range(1, i):
#         if i % j == 0:
#             res.append(j)
#     if len(res) == 1:
#         p.append(i)
# print(p)
#
# # WAP to check whether the entered number is armstrong or not.
# a = int(input('enter the number:'))
# j = a
# p = 0
# while j > 0:
#     p += 1
#     j //= 10
# i = a
# res = 0
# while i > 0:
#     res += (i % 10) ** p
#     i //= 10
# if res == a:
#     print('the entered number is an armstrong number')
# else:
#     print('the entered number is not an armstrong number')
#
# from collections import defaultdict
# # WAP to group the words WRT to the length of the words of a given string.
# a = input('enter the string:')
# res = defaultdict(list)
# a = a.split()
# for i in a:
#     res[len(i)].append(i)
# print(res)
#
# # WAP to split the given string without using split function
# a = input('enter the string:')
# res = []
# d = ''
# for i in a:
#     if i != ' ':
#         d += i
#     else:
#         res.append(d)
#         d = ''
#
# if d:
#     res.append(d)
# print(res)

