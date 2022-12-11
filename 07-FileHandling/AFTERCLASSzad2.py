x = input("File name: ")
file = open(x)
lines = 0
for line in file:
    lines+=1
file.close()
print("Number of lines:",lines)

