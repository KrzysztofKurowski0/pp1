def fun(array):
    print("Array:",array)
    x=''
    for i in array:
        x += str(i)
    y= ','.join(x)
    return y

print("String:",fun([5,4,3,2,6,5]))
