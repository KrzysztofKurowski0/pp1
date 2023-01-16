def f(dictionary,x,y):
    sum=0
    for k,v in dictionary.items():
        for i in range(len(v)):
            if v[i]>=x and v[i]<=y:
                sum+=v[i]
    return(sum)

print(f({"arr1":[4,5,6],"arr2":[7,5]},5,6))
print(f({"arr1":[2,6,5], "arr2":[7,1], "arr3":[2,9,8,1]}, 5, 10))