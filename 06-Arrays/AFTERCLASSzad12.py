z = int
i=0
array = []
while z != 's':
    if i==0:
        z = input("Enter 1st element of your array: ")
        if z !="s":
            array.append(z)
            i+=1
        else:
            break
    else:
        z = input("Enter another element of your array(Enter 's' if you want to stop): ")
        if z !="s":
            array.append(z)
            i+=1
        else:
            break

print("Your array:",array)

x = int(input("Enter your number: "))
y = 0
for i in array:
    if int(i)>x:
        y+=1
    else:
        continue

print(f"Elements in array greater than '{x}': {y}")