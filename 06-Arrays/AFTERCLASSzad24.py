array = [[-38, 19,24,11,22], [5,40,24,64,8],[-7,11,21,46,78]]
temparray=[]
for i in range(len(array[0])):
    temparray.append(array[0][i])
    array[0][i] = array[-1][i]
    array[-1][i] = temparray[i]
print(array)