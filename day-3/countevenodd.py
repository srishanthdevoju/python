def countnum():
    l=[453,-25425,214234,0,554,-55,345,2234]
    ec,oc=0,0
    for i in l:
        if i%2==0:
            ec+=1
        else:
            oc+=1
    print("Even numbers count:",ec)
    print("Odd numbers count:",oc)
countnum()
