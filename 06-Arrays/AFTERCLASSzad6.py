array1 = [4,36,12,28,9,44,5]
array2= [5,1,36]
print(f"1st Array: {array1}")
print(f"2nd Array: {array1}")
print("Not doubled: ",end="")
for i in range(len(array1)):
    for j in range(len(array2)):
        if array1[i] != array2[j]:
            a=True
        else:
            a=False
            break
    if a == True:
        print(array1[i], end=" ")
    else:
        continue
