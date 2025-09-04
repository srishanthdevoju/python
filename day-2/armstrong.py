def armstrong(num):
    for n in range(num):
        temp=n
        sum=0
        while temp>0:
            rem=temp%10
            sum+=rem*rem*rem
            temp=temp//10
        if sum==n:
            print(n)
armstrong(1000)