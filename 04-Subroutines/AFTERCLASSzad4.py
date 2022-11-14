def myrange(number,rangex,rangey):
    if number >= rangex and number <= rangey:
        myrange = True
    else:
        myrange = False
    return myrange

print(myrange(60,30,120))