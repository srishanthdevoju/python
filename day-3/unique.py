def unique():
    li=[2,4,1,3,2,4,5,7,]
    dic={}
    for i in range(len(li)):
        if li[i] in dic:
            dic[li[i]]+=1
        else:
            dic[li[i]]=1
    res=[]
    for i in dic:
        if dic[i] == 1:
            res.append(i)
    print(res)
unique()


