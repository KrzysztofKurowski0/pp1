import json
def f(age,course,average):
    number = sum = 0
    with open("data.json","r") as file:
        object = json.load(file)

    for student in object:
        if student["age"] >= age: 
            for element in student["studies"]["courses"]:
                if element["name"] == course:
                    for grade in element["grades"]:
                        sum+=grade
                    if sum/len(element["grades"]) >= average:
                        number+=1
                        sum = 0
                    else:
                        sum=0
                        break
    return number

print(f(21, "statistics", 4))
