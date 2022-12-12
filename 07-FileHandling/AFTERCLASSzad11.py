import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)
every=0
for i in temperatures:
    every+=int(i)
avarage = every/len(temperatures)

print(avarage)
