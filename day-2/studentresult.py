for i in range(1,4):
    rollno=int(input())
    sname=input()
    sub1marks=int(input())
    sub2marks=int(input())
    sub3marks=int(input())
    avg=round((sub1marks+sub2marks+sub3marks)/3,2)
    print(rollno, sname ,avg)
    if sub1marks>=40 and sub2marks >=40 and sub3marks>=40:
        if avg>80 :
            print("Distinction")
        elif 71<=avg and avg>=80:
            print("Grade","A")
        elif 51<=avg and avg>=70:
            print("Grade","B")
        else:
            print("Grade","C")   
    else:
        print("Fail") 