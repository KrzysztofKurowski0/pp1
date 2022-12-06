def median(array):
    if len(array)%2 !=0:
        i = int(len(array)/2)
        return array[i]
    else: 
        i = int(len(array)/2)
        j = int(len(array)/2) - 1
        k = (array[i] + array[j]) / 2
        return k

print(median([1,0,9,4,6]))
print(median([6,8,3,1,0,5,7]))
