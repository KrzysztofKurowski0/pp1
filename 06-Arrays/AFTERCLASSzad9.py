array = [12,5,9,1,15,16]
a=0
for i in range(len(array)-1):
    if array[i]==max(array):
        continue
    elif array[i] > a:
        a=array[i]
    else:
        continue
print(a)