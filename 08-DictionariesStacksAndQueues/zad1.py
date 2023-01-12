person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }

for key,value in person.items():
    print(key,':',value)

person['surname'] = 'Nowak'

person['married'] = False

person['gender'] = "male"

person.update({'hobby':['swimming','excursions','bicycle']})

person.update({"phone":{"landline":"123444321","mobile":"777888999","work":"313131444"}})

for key,value in person.items():
    print(key,':',value)




