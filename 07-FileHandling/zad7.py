file = open("shoppinglist.txt","a")
file.write(input("What do you want to buy next: "))
file.write("\n")
file.close()

file = open("shoppinglist.txt","r")
x=1
print("Your shopping list: ")
for line in file:
    print(f"{x}. {line}")
    x+=1
file.close()