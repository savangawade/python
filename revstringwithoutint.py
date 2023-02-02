a="sa93va45na"
lists=list(a)
i=0
j=len(lists)-1
while i<j:
    if not lists[i].isalpha():
        i+=1
    elif not lists[j].isalpha():
        j-=1
    else:
        lists[i],lists[j]=lists[j],lists[i]
        i+=1
        j-=1
rev=''.join(lists)
print(f"reveese string without number reverse:",rev)
# def reverse_string(a):
#     temp=[]
#     a=list(a)
#     for i in a:
#         if not i.isnumeric():
#             temp.append(i)
#     reverse_temp=temp[::-1]
#     count=0
#     for i in range(0,len(a)):
#         if not a[i].isnumeric():
#             a[i]=reverse_temp[count]
#             count+=1
#         else:
#             continue
#         return"".join(a)
# print(reverse_string(a))