def frequency():
    li=[4,2,3,4,6,1,3,5]
    freq={}
    for i in range(len(li)):
        if li[i] in freq:
            freq[li[i]]+=1
        else:
            freq[li[i]]=1
    x=int(input())
    if x in freq:
        print(freq[x])
frequency()
    