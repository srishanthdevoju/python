def largest(a,b,c):
    if a>b and a>c:
        return "a is greater"
    elif a>b and c>a:
        return "c is greater"
    else:
        return "b is greater"
res=largest(10,20,4)
print(res)