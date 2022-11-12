n = int(input("Range: "))
for i in range (n):
    if i%2 != 0 and i%3 != 0 and i%5 != 0 or i==5 or i==2 or i==3:
        print(i)
    else: 
        continue

