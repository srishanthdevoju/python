def division():
    num=int(input())
    deno=int(input())
    try:
        print(num/deno)
    except ZeroDivisionError:
        print("Error:Division by zero is not allowed.")
division()