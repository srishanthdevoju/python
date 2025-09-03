def vowels(c):
    vow={'a','e','i','o','u'}
    if c in vow:
        return ("Vowel")
    else:
        return ("Consonant")
res=vowels('j')
print(res)