#
# # *  *  *  *  *
# # *  *  *  *  *
# # *  *  *  *  *
# # *  *  *  *  *
# # *  *  *  *  *
# for i in range(1, 6):
#     for j in range(1, 6):
#         print('*', sep='', end='  ')
#     print()
#
# # *
# # *  *
# # *  *  *
# # *  *  *  *
# # *  *  *  *  *
# for i in range(1, 6):
#     for j in range(1, 6):
#         if i >= j:
#             print('*', sep='', end='  ')
#     print()
#
# # *  *  *  *  *
# #    *  *  *  *
# #       *  *  *
# #          *  *
# #             *
# for i in range(1, 6):
#     for j in range(1, 6):
#         if i <= j:
#             print('*', sep='', end='  ')
#         else:
#             print(' ', end='  ')
#     print()
#
# # *  *  *  *  *
# # *  *  *  *
# # *  *  *
# # *  *
# # *
# for i in range(1, 6):
#     for j in range(1, 6):
#         if i + j <= 6:
#             print('*', sep='', end='  ')
#         else:
#             print(' ', end='  ')
#     print()
# #
# #             *
# #          *  *
# #       *  *  *
# #    *  *  *  *
# # *  *  *  *  *
# for i in range(1, 6):
#     for j in range(1, 6):
#         if i + j >= 6:
#             print('*', sep='', end='  ')
#         else:
#             print(' ', end='  ')
#     print()
#
# #       *
# #       *
# # *  *  *  *  *
# #       *
# #       *
# #
# for i in range(1, 6):
#     for j in range(1, 6):
#         if i == 3 or j == 3:
#             print('*', sep='', end='  ')
#         else:
#             print(' ', end='  ')
#     print()
#
# # *  *  *  *  *
# # *           *
# # *           *
# # *           *
# # *  *  *  *  *
# for i in range(1, 6):
#     for j in range(1, 6):
#         if i in (1, 5) or j in (1, 5):
#             print('*', sep='', end='  ')
#         else:
#             print(' ', end='  ')
#     print()
# #
# #
# #     *  *  *
# #     *  *  *
# #     *  *  *
# #
# for i in range(1, 6):
#     for j in range(1, 6):
#         if i not in (1, 5) and j not in (1, 5):
#             print('*', sep='', end='  ')
#         else:
#             print(' ', end='  ')
#     print()

# #       *
# #    *  *  *
# # *  *  *  *  *
# #    *  *  *
# #       *
#
# for i in range(1, 6):
#     for j in range(1, 6):
#         if (i not in (1, 5) and j not in (1, 5)) or (i == 3 or j == 3):
#             print('*', sep='', end='  ')
#         else:
#             print(' ', end='  ')
#     print()


# # *
# # * *
# # * * *
# # * * * *
# # * * * * *
# for i in range(1, 6):
#     print(i * '* ')
# #
# # * * * * *
# #   * * * *
# #     * * *
# #       * *
# #         *
# n=5
# for i in range(n):
#     print(('  '*i)+('* '*(n-i)))
#

# #         *
# #       * *
# #     * * *
# #   * * * *
# # * * * * *
# n = 5
# for i in range(1, n+1):
#     print(('  '*(n-i))+('* ' * (i)))

# # 1
# # 2  3
# # 4  5  6
# # 7  8  9  10
# # 11  12  13  14  15
# # 16  17  18  19  20  21
# # 22  23  24  25  26  27  28
# # 29  30  31  32  33  34  35  36
# # 37  38  39  40  41  42  43  44  45
# # 46  47  48  49  50  51  52  53  54  55
# #
# n = 10
# x = 1
# for i in range(1, n+1):
#     for j in range(i):
#         print(x, end='  ')
#         x += 1
#     print()

