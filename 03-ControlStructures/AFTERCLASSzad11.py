for i in range (3):
    code=1000
    entercode=int(input("Enter the PIN code: "))
    if entercode==code:
        print("Correct!")
        break
    else:
        print("Incorrect...")
    if i==2:
        print("Sorry your payment has been blocked.")
    else:
        continue
        


