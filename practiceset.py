# a=int(input("enter number:"))
# b=int(input("enter number:"))
# print(f"before swap",a,b)
# a,b=b,a
# print(f"after swap",a,b)
###===========================================================================================
# n=int(input("enter number:"))
# count=0
# i=1
# while(i<=n):
#     if(n%i==0):
#         count=count+1
#     i=i+1
# if(count==2):
#     print(n,"is prime number")
# else:
#     print(n,"is composite number")  
##=========================================================================================
# i=int(input("enter number:"))
# fac=1
# while i>0:
#     fac=fac*i
#     i=i-1
# print("Factorial=",fac)
##==============================================================================
# arr=[45,56,78,21,49,87,68]
# max=arr[0]
# n=len(arr)
# for i in range(1,n):
#     if arr[i]>max:
#         max=arr[i]
# print("maximum value=",max)
####################################################################################

# arr=[45,56,78,21,49,87,68]
# min=arr[0]
# n=len(arr)
# for i in range(1,n):
#     if arr[i]<min:
#         min=arr[i]
# print("miniimum value=",min)
####################################################################
# n=int(input("enter number:"))
# x=0
# y=1
# z=0
# while(z<=n):
#     print(z)
#     x=y
#     y=z
#     z=x+y
###################################################################
# arr=[10,20,30,40]
# print(sum(arr))
##################################################################
# a=[]
# size=int(input("how many elements you want to enter:"))
# for i in range(size):
#     val=int(input("enter number:"))
#     a.append(val)
# sum=0
# for i in range(size):
#     sum=sum+a[i]
# print("sum of elements=",sum)
#######################################################################
# a=["savan",25,45,"pavan",78.4]
# print("Length of the list=",len(a))

# arr=[45,56,78,21,49,87,68]
# print("max number=",max(arr))
# print("min number=",min(arr))
#####################################################################################
# list=[22,44,55.66,99]
# print("list before swapping",list)
# size=len(list)
# temp=list[0]
# list[0]=list[size-1]
# list[size-1]=temp
# print("list after swapping",list)
###########################################################################
# list=[10,20,45,85,90]
# print("before swap",list)
# pos1,pos2=1,3
# list[pos1],list[pos2]=list[pos2],list[pos1]
# print("after swaapping",list)
############################################################################
# list=["bat","cricket","stump","cricket","ball","cricket","helmet"]
# word="cricket"
# n=3
# count=0
# for i in range(0,len(list)-1):
#     if(list[i]==word):
#         count=count+1
#         if(count==n):
#             list.pop(i)
# print("updated list:",list)
############################################################################
# n=int(input("enter size="))
# a=[]
# for i in range(n):
#     val=int(input("enter number="))
#     a.append(val)
# b=int(input("enter number to search="))
# flag=0
# for i in range(n):
#     if(a[i]==b):
#         flag=1
#         pos=i+1
#         break
# if(flag==1):
#     print("element found",pos,"position")
# else:
#     print("element not found")
##############################################################################
# list=[45,55,65,85]
# print("before clear",list)
# list.clear()
# print("after clear",list)
###########################################################
# list=[10,25,45,85,95]
# print("before reverse",list,)
# list.reverse()
# print("list after reverse",list)
##################################################################
# list=[10,25,45,85,95]
# print("before reverse",list,)
# list2=list[::-1]
# print("list after reverse",list2)
#######################################################
# list=[4,45,8,74,56]
# list_copy=list[:]
# print("copy list=",list_copy)
#######################################################################
# list=[45,10,23,55,45,87,45,62]
# a=45
# count=0
# for ele in list:
#     if(ele==a):
#         count=count+1
# print("{} has occured {} times".format(a,count))
############################################################################
# list=[1,2,3,4,5]
# result=1
# for i in list:
#     result=result*i
# print("Multiplication=",result)
####################################################################
# list=[10,5,80,70,50]
# list.sort()
# print(list)
# print("smallest element =",list[0])
# print("largest element =",list[-1])
#####################################################################
# list=[10,5,80,70,50]
# list.sort()
# print(list)
# print("second largest element=",list[-2])
#################################################################
# a=input("enter a string:")
# print(a[:])
# revstr=(a[::-1])
# if revstr==a:
#     print(a," is Palindrome")
# else:
#     print(a,"is not palindrome")
################################################################
# str="Welcome to India"
# word=str.split(" ")
# print("Original str",word)
# word=word[-1::-1]
# print("reverse",word)
# outputstr=' '.join(word)
# print("reverse str:",outputstr)
#####################################################################
# str="Welcome to India"
# sub_str="India"
# print(str.find(sub_str))
##################################################################
# str="Welcome to India"
# counter=0
# for i in str:
#     counter=counter+1
# print("length of str=",counter)
##################################################################
# import re
# str="welcome@#*to%@!India#$%"
# regex=re.compile('[!@#$%^&*()~]')
# if(regex.search(str)==None):
#     print("No special character present in a string")
# else:
#     print("Special character present in string")
###########################################################################
import re
str="Im photographer at https://www.pixpa.com/examples/photography"
url=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',str)
print("url is:",url)