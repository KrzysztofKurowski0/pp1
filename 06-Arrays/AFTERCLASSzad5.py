def compare(array1,array2):
    for i in range(len(array1)):
        if len(array1) != len(array2):
            a=False
            break
        elif len(array1) == len(array2) and array1[i] == array2[i]:
            a = True
        else:
            a = False
            break
    return a

if compare(["water","book","sky"],["water","book","sky"]) == True:
    print("Both arrays are the same")
else:
    print("Arrays are not the same")

