import random
with open("randomint.txt","w") as randomint:
    for i in range(1,51):
        if i<50:
            randomint.write(f"{random.randint(100,999)}\n")
        else:
            randomint.write(f"{random.randint(100,999)}")