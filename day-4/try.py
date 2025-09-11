try:
    print(10/0)
except ArithmeticError:
    print("ArithmeticError")
else:
    print("no Error")
finally:
    print("THIS IS EXCEPTION HANDLING")