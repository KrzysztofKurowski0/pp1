print("Let's play a guess game. Select a number from 1 to 6")
import random
dice=random.randint(1,6)
guess=int(input())
if dice==guess:
    print(True)
else:
    print(False)

