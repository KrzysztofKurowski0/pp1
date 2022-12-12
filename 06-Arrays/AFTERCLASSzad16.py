array=[]
for i in range(1,1000):
    array.append(i)
print("-----------------------------------------")
for i in array:
    if i%8 != 0:
        print(f"| {i}",end="")
    else:
        print(f"| {i}")
print("\n-----------------------------------------")