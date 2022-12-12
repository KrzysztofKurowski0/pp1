array1 = [1,2,3,4,5]
array2 =[3,4,2,1,5]
for i in range(len(array1)):
    for j in range(len(array2)):
        if array1[i] == array2[j]:
            x=True
            break
        else:
            x=False
    if x==False:
        y=False
        break
    else:
        y=True

print(y)