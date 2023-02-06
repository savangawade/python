# n=int(input("enter number="))
# for i in range(n):
#     for j in range(i+1):
#         print(j+1,end=' ')
#     print()

# n=int(input("enter number="))
# for i in range(n):
#     for j in range(i,-1,-1):
#         print(j+1,end=' ')
#     print()

# n=int(input("enter number="))
# for i in range(n):
#     for j in range(i,-1,-1):
#         print(i+1,end=' ')
#     print()

# n=int(input("enter number="))
# for i in range(n):
#     for j in range(i,-1,-1):
#         print(n-i,end=' ')
#     print()

# n=int(input("enter number="))
# for i in range(n):
#     for j in range(i-1-1):
#         print(n-j,end=' ')
#     print()

# n=int(input("enter number="))
# for i in range(n):
#     for j in range(i+1):
#         print(n-j,end=' ')
#     print()

# n=int(input("enter number="))
# for i in range(n):
#     for j in range(n-i-1):
#         print(' ',end=' ')
#     for j in range(i,-1,-1):
#         print(j+1,end=' ')
#     print()

# n=int(input("enter number="))
# for i in range(n):
#     for j in range(i,-1,-1):
#         print(j+1,end=' ')
#     print()

# n=int(input("enter number="))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end='')
#     for j in range(i,-1,-1):
#         print(j+1,end=' ')
#     print()

# n=int(input("enter number="))
# for i in range(n-1,-1,-1):
#     for j in range(n-i-1):
#         print(" ",end='')
#     for j in range(i,-1,-1):
#         print(j+1,end=' ')
#     print()

#n=int(input("enter number="))
# for i in range(4):
#     for j in range(4-i-1):
#         print(" ",end='')
#     for j in range(i+1):
#         print('* ',end='')
#     for j in range(2*(4-i-1)):
#         print(" ",end='')
#     for j in range(i+1):
#         print('* ',end='')
#     print()
# for i in range(8,0,-1):
#     for j in range(8-i):
#         print(' ',end='')
#     for j in range(i,0,-1):
#         print('* ',end='')
#     print()


# n=int(input("enter number="))
# x=int(input("enter another number="))    # x should be 2n
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end='')
#     for j in range(i+1):
#         print('* ',end='')
#     for j in range(2*(n-i-1)):
#         print(" ",end='')
#     for j in range(i+1):
#         print('* ',end='')
#     print()
# #x=2*n
# for i in range(x,0,-1):
#     for j in range(x-i):
#         print(' ',end='')
#     for j in range(i,0,-1):
#         print('* ',end='')
#     print()

for row in range(6):
    for col in range(7):
        if(row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
            print('*',end=' ')
        else:
            print(" ",end=' ')
    print()
        
























