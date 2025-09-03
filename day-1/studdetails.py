for i in range(1,4):
    rollno=int(input())
    sname=input()
    sub1marks=int(input())
    sub2marks=int(input())
    sub3marks=int(input())
    avg=round((sub1marks+sub2marks+sub3marks)/3,2)
    print(rollno, sname ,avg)