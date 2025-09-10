def secondlargest():
    li=[423,233,-44,20,40,0]
    fi=li[0]
    for i in li:
        if i>fi:
            fi=i
    li.remove(fi)
    se=li[0]
    for i in li:
        if i>se:
            se=i
    print(se)
secondlargest()