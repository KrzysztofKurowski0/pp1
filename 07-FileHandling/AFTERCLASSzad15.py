import re
with open("grades.txt","r") as file:
    content = file.read()
    words=re.findall("\d.\d",content)
    print(f"Student's grades: {words}")
    all=0
    for i in words:
        all+=float(i)
arithmeticmean = round(all/len(words),2)
print(f"Arithmetic mean: {arithmeticmean}")
