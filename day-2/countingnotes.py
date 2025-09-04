def counting(a):
    rem=a//2000
    print("No of 2000 notes",rem)
    a=a-2000*rem
    rem=a//500
    print("No of 500 notes",rem)
    a=a-500*rem
    rem=a//200
    print("No of 200 notes",rem)
    a=a-200*rem
    rem=a//100
    print("No of 100 notes",rem)
    a=a-100*rem
    rem=a//50
    print("No of 50 rs notes",rem)
res=counting(3400)
