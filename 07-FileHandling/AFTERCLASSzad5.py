with open("sample.txt","r") as file:
    with open("copylines.txt","w") as file2:
        for i in file:
            file2.write(i)