list=[15,"Savan","Pavan",14,45]
print("list before reverse=",list)
newlist=[]
for i in range(1,len(list)+1):
    newlist.append(list[-i])
print("reverse list=",newlist)
print("program is done")