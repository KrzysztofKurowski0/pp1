class C():
    def __init__(self):
        self.evennumbers = ""

    def m1(self,number):
        a=[]
        listed = list(str(number))
        for i in range(len(listed)):
            if int(listed[i]) %2 == 0:
                self.evennumbers+=(str(listed[i]))
            else:
                continue
        return int(self.evennumbers)

    def m2(self,n):
        listed = list(str(n))
        for i in range(len(listed)):
            if i == 0:
                continue
            else:
                if int(listed[i]) >= int(listed[i-1]):
                    self.issub = True
                else:
                    self.issub = False
                    break
        
        return self.issub

    def m3(self,n):
        self.missingnumbers = ""
        numbers = ["0","1","2","3","4","5","6","7","8","9"]
        for i in numbers:
            if i in n:
                continue
            else:
                self.missingnumbers+=i

        return self.missingnumbers


c = C()
c.m1("12340")
c.m2("12340")
c.m3("12340")

