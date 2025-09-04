def weeks(x):
    if x=='1':
        return ("Sunday")
    elif x=='2':
        return ("Monday")
    elif x=='3':
        return ("Tuesday")
    elif x=='4':
        return ("Wednesday")
    elif x=='5':
        return ("Thursday")
    elif x=='6':
        return ("Friday")
    else:
        return ("Saturday")
res=weeks('4')
print(res)