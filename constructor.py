class Addition:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def sum(self):
        z=self.a+self.b+self.c
        print("sum is:",z)
while True:
    a=int(input("enter first number:"))
    b=int(input("enter second number:"))
    c=int(input("enter third number:"))
    obj=Addition(a,b,c)
    obj.sum()









