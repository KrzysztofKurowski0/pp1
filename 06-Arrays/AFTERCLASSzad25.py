array = [[-38, 19,24,11,22], [5,40,24,64,8],[-7,11,21,46,78]]
temparray=[]
for i in range(len(array)):
    temparray = array[i][0]
    array[i][0] = array[i][-1]
    array[i][-1]=temparray


print(array)