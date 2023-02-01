a="sa93va45n"
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