def divisors(num):
    l = []
    for i in range(1, num):
        if num % i == 0:
            l.append(i)
    return sum(l)

def perfect(numb):
    for n in range(1, numb+1):
        if n == divisors(n):
            print(n)

perfect(1000)
