def string():
    s=input()
    dict={}
    for i in s:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    for k in sorted(dict):
        s=max(k,k=dict.values())
string()
