def ecommerceapp():
    l=[]
    while True:
        print("Enter any choice ->1. 2. 3. 4. 5. 6.")
        print("1.Add a product to the cart.")
        print("2.Remove a product from the cart")
        print("3.Search for a product in the cart" )
        print("4.Display all products in the cart")
        print("5.Show the total number of products in the cart")
        print("6.ALphabetical order")
        print("7.clear")
        inp=int(input())
        if inp==1:
            x=input("Enter product to be added:")
            l.append(x)
        elif inp==2:
            x=input("Enter product to be removed:")
            l.remove(x)
        elif inp==3:
            x=input("Enter product to be searched:")
            if x in l:
                print("product{",x, "}found")
            else:
                print("product{",x,"}not found")
        elif inp==4:
            print("Displaying cart:",l)
        elif inp==5:
            print("Total products:",len(l))
        elif inp==6:
            print(sorted(l))
        elif inp==7:
            l.clear()
        else:
            break
ecommerceapp()

        