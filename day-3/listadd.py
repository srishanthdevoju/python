def add():
    l=[]
    l.append("apple")
    l.insert(1,"banana")  
    print(l)
    l2=[]
    n=int(input())
    for i in range(n):
        inp=int(input())
        l2.append(inp)
    print(l2)
add()