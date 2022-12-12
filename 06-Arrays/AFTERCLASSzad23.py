array = [[-38, 19],[5,40],[-7,11],[29,16]]
x=array[0][0]
y=array[0][0]
for row in array:
    for i,col in enumerate(row):
        if row[i]>x:
            x=row[i]
        else:
            continue

for row in array:
    for i,col in enumerate(row):
        if row[i]<y:
            y=row[i]
        else:
            continue

print(f"Highest number: {x}")
print(f"Lowest number: {y}")
