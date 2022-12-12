def create_2d_arr(x,y):
    array = [[0 for i in range(y)] for j in range(x)]
    return array

print(create_2d_arr(3,5))