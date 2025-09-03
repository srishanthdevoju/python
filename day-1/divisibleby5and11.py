def divisible(num):
    if num%5==0 and num%11==0:
        return True
    else:
        return False
res=divisible(55)
print(res)