def occurs(number, array):
    if array.count(number) >= 1:
        return True
    else:
        return False

number = int(input("Enter your number: "))
array = []
for i in range (4):
    array.append(int(input("Array: ")))
y = occurs(number,array)
if y == True:
    print(f"Number {number} appears in the array6")
else:
    print(f"Number {number} does not appear in the array")

