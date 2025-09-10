def alphabets():
    st=input()
    vc=0
    cc=0
    v=['a','e','i','o','u']
    for i in st.lower():
        if i in v:
            vc+=1
        else:
            cc+=1
    return [vc,cc]
res=alphabets()
print(res)