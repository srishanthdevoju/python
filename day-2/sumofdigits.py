def sumofdigits(num):
    tot=0
    while num>0:
        rem=num%10
        tot+=rem
        num=num//10
    return tot
res=sumofdigits(1234)
print(res)

