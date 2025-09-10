def wordcount():
    c=1
    s=input()
    for i in range(len(s.strip())):
        if s[i]==" " and s[i-1]!=" ":
            c+=1
    return c
res= wordcount()
print(res)  