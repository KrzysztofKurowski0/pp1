import stack
def RPN(expression):
    number = ['1','2','3','4','5','6','7','8','9','0']
    operator =['+','-','*','/']
    result = ''
    for i in range(len(expression)):
        if expression[i] in number:
            stack.push(expression[i])
        elif expression[i] in operator:
            reversed1=stack.pop()
            reversedsign=expression[i]
            reversed2=stack.pop()
            reversed = '('+reversed2+reversedsign+reversed1+')'
            stack.push(reversed)
        else:
            while stack.empty() == False:
                result+=stack.pop()
    return result
            

print(RPN('831+/32-4+*='))