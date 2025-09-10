def characters():
    x=input()
    a=0
    d=0
    sp=0
    for i in x:
        if i.isalpha():
            a+=1
        elif i.isdigit():
            d+=1
        else:
            sp+=1
    return[a,d,sp]
res=characters()
print(res)