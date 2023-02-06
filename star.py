# # a="*"
# # tempType=type('*')
# # print(tempType)
# a=10
# print(type(a))
#print( not None!=True)
#print(not True!=False)
# n=5
# for i in range(n):
#     for j in range(n):
#         print('*',end='')
#     print()
###############################################################
n=3
for i in range(n):
    for j in range(i):
        print('*',end=' ')
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i+n-2):
        print('*',end=' ')
    print()
for i in range(n):
    for j in range(n-i):
        print('*',end=' ')
    print()

# n=3
# for i in range(n):
#     for j in range(i+1):
#         print('',end=' ')
#     for j in range(i):
#         print('*',end=' ')
#     for j in range(i,n-1):
#         print('*',end=' ')
#     print()

# n=3
# for i in range(n):
#     for j in range(i,n-1):
#         print('',end=' ')
#     for j in range(i,):
#         print('*',end=' ')
#     for j in range(i+1):
#         print('*',end=' ')
#     print()
#Diamond
# n=3
# for i in range(n-1):
#     for j in range(n-i):
#         print(' ',end=' ')
#     for j in range(i):
#         print('*',end=' ')
#     for j in range(i+1):
#         print('*',end=' ')
#     print()
# for i in range(n):
#         for j in range(i+1):
#          print(' ',end=' ')
#         for j in range(i,n-1):
#          print('*',end=' ')
#         for j in range(i,n):
#          print('*',end=' ')
#         print()

# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(' ',end='')
#     for j in range(i):
#         print('*',end='')
#     for j in range(i+1):
#         print('*',end='')
#     print()