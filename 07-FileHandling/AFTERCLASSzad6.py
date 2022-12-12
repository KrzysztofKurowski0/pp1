with open("MeatAndFish.txt","r") as file1:
    length = len(file1.readlines())
    x=1

with open("MeatAndFish.txt","r") as file1:
    with open("GrainsAndBread.txt","r") as file2:
        with open("nextshoppinglist.txt","w") as shopping:
            for i in file1:
                if x == length:
                    shopping.write(f"{i}\n")
                    x+=1
                else:
                    shopping.write(i)
                    x+=1
            for j in file2:
                shopping.write(j)
        