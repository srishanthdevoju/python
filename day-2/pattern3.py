for i in range(5):
    for j in range(5):
        if i==j or i==5-j-1:
            print('$',end=" ")
        else:
            print('*',end=" ")
    print()