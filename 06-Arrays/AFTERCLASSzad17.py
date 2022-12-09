array1 = [1,2,3,4,5]
array2 =[1,2,3,4,5]
for i in range(len(array1)):
    for j in range(len(array2)):
        if array1[i] == array2[j]:
            x = True
            break
        else:
            x = False
            break

print(x)