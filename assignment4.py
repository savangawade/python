aValue=input("enter the string=")
bValue=input("enter the character from aValue=")
Result=aValue.find(bValue)
print(f"find of chracter in {bValue}:{Result}")
Result=aValue.find(bValue,3,7)
print(f"find of character in {bValue}:{Result}")
result=aValue.count(bValue)
print(f"count of bvalue in {bValue}:{result}")

a=eval(input())