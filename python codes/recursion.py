# def rep(i=0):
#     if i >= 5:
#         return None
#     else:
#         print('hello world')
#         return rep(i=i+1)

# scope of a variable:
# LEGB(L:- Local, E:- Enclosed, G:- Global, B:- Built-in)


x = 199
y = 299


def add():
    a = 10
    b = 20
    print(a + b)
    a = 199
    print(y)
    x = x + 999


add()
