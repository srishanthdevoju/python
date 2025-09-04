def factors(num):
    l=[]
    for i in range(1,num):
        if num % i == 0:
            l.append(i)
    return l
res=factors(20)
print(*res,end=" ")
