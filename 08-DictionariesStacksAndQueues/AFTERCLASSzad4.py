import json
with open ("euro.json","r") as rfile:
    content = json.load(rfile)
    print("Date",end="                    ")
    print("Buying Rate",end="                    ")
    print("Selling Rate")
    print("="*68)
    for i in range(10):
        print(content["rates"][i]["effectiveDate"],end="              ")
        print(round(content["rates"][i]["ask"],3),end="                          ")
        print(content["rates"][i]["bid"])