
# *  *  *  *  *
# *  *  *  *  *
# *  *  *  *  *
# *  *  *  *  *
# *  *  *  *  *
for i in range(1, 6):
    for j in range(1, 6):
        print('*', sep='', end='  ')
    print()

# *
# *  *
# *  *  *
# *  *  *  *
# *  *  *  *  *
for i in range(1, 6):
    for j in range(1, 6):
        if i >= j:
            print('*', sep='', end='  ')
    print()

# *  *  *  *  *
#    *  *  *  *
#       *  *  *
#          *  *
#             *
for i in range(1, 6):
    for j in range(1, 6):
        if i <= j:
            print('*', sep='', end='  ')
        else:
            print(' ', end='  ')
    print()

# *  *  *  *  *
# *  *  *  *
# *  *  *
# *  *
# *
for i in range(1, 6):
    for j in range(1, 6):
        if i + j <= 6:
            print('*', sep='', end='  ')
        else:
            print(' ', end='  ')
    print()
#
#             *
#          *  *
#       *  *  *
#    *  *  *  *
# *  *  *  *  *
for i in range(1, 6):
    for j in range(1, 6):
        if i + j >= 6:
            print('*', sep='', end='  ')
        else:
            print(' ', end='  ')
    print()

#       *
#       *
# *  *  *  *  *
#       *
#       *
#
for i in range(1, 6):
    for j in range(1, 6):
        if i == 3 or j == 3:
            print('*', sep='', end='  ')
        else:
            print(' ', end='  ')
    print()

# *  *  *  *  *
# *           *
# *           *
# *           *
# *  *  *  *  *
for i in range(1, 6):
    for j in range(1, 6):
        if i in (1, 5) or j in (1, 5):
            print('*', sep='', end='  ')
        else:
            print(' ', end='  ')
    print()
#
#
#     *  *  *
#     *  *  *
#     *  *  *
#
for i in range(1, 6):
    for j in range(1, 6):
        if i not in (1, 5) and j not in (1, 5):
            print('*', sep='', end='  ')
        else:
            print(' ', end='  ')
    print()
