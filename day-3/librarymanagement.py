def library():
    dict={}
    dict[1]='English'
    dict[2]='Science'
    dict[3]='Maths'
    dict[4]='Maths'
    dict.pop(4)
    print(dict)
    dict.update({3:"Telugu"})
    print(dict)
    for i in dict.values():
        print(i,end=" ")
    c=0
    print()
    for i in dict.values():
        c+=1
    print("Book Count:",c)
    x=(input())
    for i in dict.values():
        if i==x:
            print("Yes, Exist")
library()
