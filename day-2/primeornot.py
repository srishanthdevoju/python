def prime(num):
    if num<2:
        return "Not Prime"
    for i in range(2,num):
        if num%i==0:
            return "Not Prime"
    return "Prime"
res=prime(21)
print(res)