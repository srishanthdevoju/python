def leap(num):
    if num%4!=0:
        return ("Not a Leap year")
    if num %100==0:
        return ("Not a Leap year")
    if num%400==0:
        return ("Not a Leap year")
    else:
        return ("Leap year")
y=leap(2100)
print(y)