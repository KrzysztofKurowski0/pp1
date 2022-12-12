def matrix(n):
    for row in range(0, n):
        for col in range(0, n):
            if (row == col):
                print("1 ", end=" ")
            else:
                print("0 ", end=" ")
        print()
matrix(3)
matrix(5)
matrix(8)

