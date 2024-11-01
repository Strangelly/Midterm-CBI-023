def func(str1):
    str2 = ''
    for x in str1:
        if x in str2:
            pass
        else:
            str2+=x
    return str2


x = input()
print(func(x))