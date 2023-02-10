# n=int(input("enter the number="))
# result=1
# for i in range(n,0,-1):
#     result=result*i
# print("factorial of",n,"is=",result)



# n=int(input("enter the number="))
# fact=1
# if n>0:
#     for i in range(1,n+1):
#         fact=fact*i
# print("factorial of",n,"is=",fact)


# n=int(input("enter the number="))
# count=2
# fact=1
# while (count<=n):
#     fact=fact*count
#     count=count+1
# print("factorial of",n,"is=",fact)


n=int(input("enter the number="))
count = 1
fact=1
while (count<n):
    fact=fact*n
    n=n-1
print("factorial of number","is=",fact)
