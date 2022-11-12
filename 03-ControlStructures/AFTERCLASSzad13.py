array = []

ele=1
count=0
while ele != 0:
    ele = int(input("Enter a number: "))
    array.append(ele)
    count+=1

sum = sum(array)
mean = sum/(count-1)

print(f"RESULT: Quantity = {count - 1}, Sum = {sum}, Mean = {mean}")

    