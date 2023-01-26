def f1(t):
    splitted = t.split()
    a = splitted.count("is")
    print(a)
    for i in range(len(splitted)):
        if splitted[i] == "is":
            dict = {splitted[i-1]:int(splitted[i+1])}
    print(type(dict))
    return dict
    
print(f1("Mark is 24 and Ann is 27"))
