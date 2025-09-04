def firstandlast(num):
    last=num%10
    first=num
    while first>=10:
        first=first//10
    return (first,last)
res=firstandlast(123)
print(res)