def countdigits(num):
    c=0
    while num>0:
        c+=1
        num=num//10
    return c
res=countdigits(42874)
print(res)
