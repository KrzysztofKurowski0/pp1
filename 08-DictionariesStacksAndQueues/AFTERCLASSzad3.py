import json
with open("students.json","r") as file:
    content = json.load(file)

    with open("limited.json","w") as wfile:
        for name in content:
            for element in name["name"]:
                a = json.dumps(element)
                wfile.write(a)
            




        
