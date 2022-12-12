def convert(array):
    array1d=[]
    for i in range(len(array)):
        for j in range(len(array[0])):
            x = array[i][j]
            array1d.append(x)
    return array1d
  
print(convert([[2,1],[3,5]]))
print(convert([[2,1],[3,5],[7,4],[2,6]]))