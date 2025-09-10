def string():
    s = input()
    count = {}
    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    max_char = max(count, key=count.get)
    print(max_char, count[max_char])

string()
