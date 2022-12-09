def f(array):
    x=[]
    for i in array:
        if i%2 == 0:
            x.append(i)
        else:
            continue
    for j in array:
        if j%2 != 0:
            x.append(j)
        else:
            continue
    return x

print(f([7,0,4,2,5,0,3]))
