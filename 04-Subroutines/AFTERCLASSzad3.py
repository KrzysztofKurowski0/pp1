def sum(x):
    length=len(str(x))
    mylist=list(str(x))
    sum = 0
    for i in range(length):
        sum += int(mylist[i])
    
    return sum

print(sum(7182))
