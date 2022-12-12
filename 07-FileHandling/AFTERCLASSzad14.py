import re
with open("sample.txt","r") as file:
    content = file.read()
    words=re.findall("\w+",content)
    for i in range (len(words)):
        if len(words[i])>=6:
            print(words[i])
        else:
            continue
