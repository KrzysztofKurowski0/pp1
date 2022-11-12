money = int(input("Enter the amount in PLN: "))
print(f"The amount of PLN",money,"in coins: " )

five = 0
two = 0
one = 0

while money >= 5:
    money -= 5
    five += 1

while money >= 2 and money < 5:
    money -= 2
    two += 1

while money == 1:
    money -= 1
    one += 1

print(f"5 zl: ",five)
print(f"2 zl: ",two)
print(f"1 zl: ",one)



