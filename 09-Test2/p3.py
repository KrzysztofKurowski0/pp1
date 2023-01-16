def f(array2D):
    array=[]
    sum=0
    for j in range(len(array2D[0])):
        for i in range(len(array2D)):
            sum+=array2D[i][j]
        array.append(sum)
        sum=0
    return array

print(f([[3,6,2,7],[9,5,4,0],[2,8,0,9]]))
            
            
