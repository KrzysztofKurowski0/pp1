def calc(x,text):
    count=0
    length = len(text)
    mylist = list(text)
    for i in range (length):
        if x == text[i]:
            count+=1
        else:
            continue
    return count

print(calc("e","You never get a second chance to make a first impression"))
            


