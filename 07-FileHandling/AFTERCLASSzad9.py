with open("numberspower","w") as power:
    for i in range(1,11):
        power2=i*i
        power3=i*i*i
        if i<10:
            power.write(f"{i},{power2},{power3}\n")
        else:
            power.write(f"{i},{power2},{power3}")