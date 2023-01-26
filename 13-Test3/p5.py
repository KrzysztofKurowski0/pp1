class C():
    def __init__(self,values):
        self.valuess = values
    
    def __str__(self):
        output = ""
        suma = str(sum(self.valuess))
        for i in self.valuess:
            if i != max(self.valuess):
                output+=str(i) + "+"
            else:
                output+=str(i)
        return f"{output}={suma}"
    
