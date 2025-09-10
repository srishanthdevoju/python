def duplicates():
    li=[1,2,34,2,3,3,2,4,23,34,2]
    dic={}
    res=[]
    for i in li:
        if i not in dic:
            dic[i]=True
            res.append(i)
    print(res)
duplicates()