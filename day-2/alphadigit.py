def input(x):
    if x.isdigit():
        return ("Number")
    elif x.isalpha():
        return ("Alphabet")
    else:
        return ("Special character")
res=input("O")
print(res)