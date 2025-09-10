def delete():
    l=[453,-25425,214234,0,554,-55,345,2234]
    x=3
    li=[]
    for i in range(len(l)):
        if i==x:
            continue
        else:
            li.append(l[i])
    print(li)
delete()