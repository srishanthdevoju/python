def fact(rem):
    if rem==1:
        return 1
    if rem==0:
        return 0
    else:
        return rem*(fact(rem-1))
def strongnum(num):
    for n in range(num):
        temp=n
        sum=0
        while temp>0:
            rem=temp%10
            sum+=fact(rem)
            temp=temp//10
        if sum==n:
            print(n)
strongnum(1000)

