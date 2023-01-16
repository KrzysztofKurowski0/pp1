array = ["Genowefa","Onufry","Celestyna","Alojzy","Pankracy"]
count = 0
name = ""
for i in range(len(array)):
    if len(array[i])>count:
        count = len(array[i])
        name = array[i]
    else:
        continue
print(name)