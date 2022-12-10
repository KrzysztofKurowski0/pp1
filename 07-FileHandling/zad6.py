array=["Sword Art Online - Progressive","Titanic","Avatar","Kubuś Puchatek","Dywizjon 303"]
file = open("film_titles.txt","w")
for i in array:
    if i == array[-1]:
        file.write(f"{i}")
    else:
        file.write(f"{i}\n")
file.close()

file = open("film_titles.txt","r")
print(file.read())
file.close()