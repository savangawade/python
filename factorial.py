# n=int(input("enter the number="))
# result=1
# for i in range(n,0,-1):
#     result=result*i
# print("factorial of",n,"is=",result)



n=int(input("enter the number="))
fact=1
if n>0:
    for i in range(1,n+1):
        fact=fact*i
print("factorial of",n,"is=",fact)
