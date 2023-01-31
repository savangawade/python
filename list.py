color=['red','blue','green','black','violet','yellow']
# print(color[0:3])
# newitem='white'
# color[3]=newitem
# print(color,type(color))
# print(color[::-1])
# print(color[::-2])
# print(color[::2])
# print(len(color))
# print(f"list before sort{color}")
# result=color.sort()
# print(f"list after sort{color}:result:{result}")  #list after sort['black', 'blue', 'green', 'red', 'violet', 'yellow']:result:None
# print(f"list before sort{color}")
# result=color.sort(reverse=True)
# print(f"list after sort{color}:result:{result}")     #list after sort['yellow', 'violet', 'red', 'green', 'blue', 'black']:result:None
Values=[10,45,49,98,88,56]
# print(f"list before reverse{Values}")
# result=Values.reverse()
# print(f"list after reverse{Values}:result:{result}")
#result=Values.insert(2,200)
#print(f"list after insert {Values}:result:{result}")  #list after insert [10, 45, 200, 49, 98, 88, 56]:result:None
#result=Values.pop(2)
#print(f"list after pop{Values}:result:{result}") #list after pop[10, 45, 98, 88, 56]:result:49
#result=Values.remove(98)
#print(f"list after remove{Values}:result:{result}")  #list after remove[10, 45, 49, 88, 56]:result:None
result=Values.append(75)
print(f"list after add{Values}:result:{result}")
