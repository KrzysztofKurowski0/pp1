import json
book = {
    "title":"Sword Art Online",
    "author":"Reki Kawahara",
    "Release_date":2010,
    "genere":"Light Novel",
    "personal rating":"9/10"
}

file = open("favourite.json","w")
json.dump(book,file)