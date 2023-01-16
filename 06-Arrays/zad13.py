array = [[3,9,2],[2,4,5],[7,1,6],[0,4,8]]
sum = 0
for i in range(len(array)):
    for j in range(len(array[1])):
        if array[i][j] %2 == 0:
            sum += array[i][j]
        else:
            continue

print(sum)