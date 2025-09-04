def factors(num):
    l=[]
    for i in range(1,num+1):
        if num % i == 0:
            l.append(i)
    return l
def prime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
def primefac(num):
    li=[]
    for f in factors(num):
        if prime(f):
            li.append(f)    
    return li
res=primefac(10)
print(res)