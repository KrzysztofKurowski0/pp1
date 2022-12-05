array = [2,3,1,2,4,4,6,7,5,3]
print(f"Array: {array}")
print(f"Unique elements: ", end="")
for i in array:
    if array.count(i) >= 2:
        continue
    else:
        print(i,end=" ")
