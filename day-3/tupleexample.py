def tupleex():
    t=[]
    for i in range(5):
        rollo=int(input())
        name=input()
        marks=float(input())
        t.append((rollo,name,marks))
    print(t)
    highest=max(t,key=lambda x:x[2])
    print("student is ",highest[1]," which is",highest[2])
    for rollo, name, marks in t:
        if marks > 75:
            print(name, "->", marks)
tupleex()