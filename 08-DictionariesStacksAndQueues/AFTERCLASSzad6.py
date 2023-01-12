import stack
def binary(decimal):
    for i in range(decimal):
        if decimal != 0:
            reminder = decimal%2
            stack.push(int(reminder))
            if decimal %2 == 0:
                decimal = decimal/2
            else:
                decimal = decimal/2 -0.5
        else:
            break
    x = ''
    while stack.empty()==False:
        x+=str(stack.pop())
    return x
    
decimal1 = int(input("Decimal number: "))
print("Binary number: ",binary(decimal1))

        
