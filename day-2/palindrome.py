def palindrome(n):
    l=[]
    for i in range(n):
        if str(i)==str(i)[::-1]:
            l.append(i)
    print(l)
res=palindrome(1000)
