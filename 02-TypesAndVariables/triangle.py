a = float(input("Set a 1st length: "))
b = float(input("Set a 2nd length: "))
c = float(input("Set a 3rd length: "))

s = (a+b+c)/2

import math
area = float(math.sqrt(s*(s-a)*(s-b)*(s-c)))

print(area)