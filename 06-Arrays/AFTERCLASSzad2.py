array = [8,2,5,1,9]
print(f"Array: {array}")
print("2nd power: ",end="")
for i in range(len(array)):
    power = array[i]*array[i]
    print(power, end=" ")
