#using third variable
#a=20
#b=30
#temp=a
#a=b
#b=temp 
#print("after swapping")
#print("a:",a)
#print("b:",b)

#without third variable
#a=20
#b=30
#a=a+b;
#b=a-b;
#a=a-b;
#print("after swapping")
#print("a:",a)
#print("b",b)
#########################################################
#a=15
#b=25
#a,b=b,a
#print(a)
#print(b)
####XOR
#a=20
#b=40
#a=a^b
#b=a^b
#a=a^b
#print(a)
#print(b)
########################################
#input
a=int(input("enter number in a:"))
b=int(input("enter number in b:"))
print("original numberis:", a,b)
a,b=b,a
print("after swapping :" ,a,b)