def f(human_age):
    dogs_years=0
    if human_age<=2:
        for i in range(human_age):
            dogs_years+=10
    else:
        for i in range(2):
            dogs_years += 10
        human_age-=2
        for i in range(human_age):
            dogs_years+=4
    return dogs_years

        

