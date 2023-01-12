import json
with open("sample2.json") as file:
    content = json.load(file)

for k,v in content.items():
    print(k,":",v)
