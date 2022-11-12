normalage = int(input("Enter the dog's age in human years: "))
dogage = 0


if normalage == 1:
    dogage+=10.5

else:
    for i in range (2):
        dogage += 10.5


    for i in range (normalage - 2):
        dogage += 4

print(f"The dog's age in dog's years is ",dogage)