with open("sample3.txt","r") as file:
    content = file.read()
    with open("copy.txt","w") as file2:
        file2.write(content)