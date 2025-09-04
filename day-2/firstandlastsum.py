def firstandlastsum(num):
    last=num%10
    first=num
    while first>=10:
        first=first//10
    return (first+last)
res=firstandlastsum(123)
print(res)