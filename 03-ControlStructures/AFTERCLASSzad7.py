for i in range (30):
    if (i+1)%3 ==0 and (i+1)%5 == 0:
        print ("BINGO", end=" ")
    elif (i+1)%5 == 0:
        print("FIVE", end=" ")
    elif (i+1)%3 == 0:
        print("THREE", end=" ")
    else:
        print(i+1, end=" ")
    

    
