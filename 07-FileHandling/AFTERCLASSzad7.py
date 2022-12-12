with open("intnumbers.txt","w") as numb:
    for i in range(1,51):
        if i<50:
            numb.write(f"{i}\n")
        else:
            numb.write(f"{i}")
