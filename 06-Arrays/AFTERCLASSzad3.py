array = [15,8,31,47,2,19]
print(f"Array: {array}")
sum=0
for i in array:
    sum+=i
print(f"Sum: {sum}")
armean = int(sum/len(array))

print(f"Arithmetic mean: {armean}")