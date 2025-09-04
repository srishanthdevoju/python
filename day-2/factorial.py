def fact(n):
    f=1
    for i in range(n,0,-1):
        f=f*i
    return f
res=fact(5)
print(res)