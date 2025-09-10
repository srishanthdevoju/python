def string():
    s=(input())#aaabbca -> #a4b2c1
    dict={}
    for i in s:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    for k in sorted(dict):
        print(k,end="")
        print(dict[k],end="")
string()