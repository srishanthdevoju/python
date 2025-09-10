def negative():
    n=int(input())
    l2=[]
    for i in range(n):
        inp=int(input())
        l2.append(inp)
    for i in range(n):
        if l2[i]<0:
            print("negative numbers:",l2[i])
negative()