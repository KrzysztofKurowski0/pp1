import json
student = {
    "name":"Krzysztof",
    "surname":"Kurowski",
    "age":20,
    "marriage":False,
    "location":["-123","87"],
    "Grades":[5,1,4,6,2,4,2,4,5,2],
    "University":"UEK w Krakowie",
    "Profile":"Informatyka stosowana"
}

file = open("student.json","w")
json.dump(student,file)