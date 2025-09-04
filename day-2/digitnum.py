def digitnum(num):
    words=["zero","one","two","three","four","five","six","seven","eight","nine"]
    for i in str(num):
        print(words[int(i)],end=" ")
res=digitnum(480)
