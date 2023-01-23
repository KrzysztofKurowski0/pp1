import random

class Thermometer():
    def __init__(self):
        self.ison = False
        self.temperature = 0

    def Measure(self):
        if self.ison:
            self.temperature = round(random.uniform(34,42),1)
        else:
            print("You must turn on the thermometer!")

    def on(self):
        self.ison = True
    
    def off(self):
        self.ison = False

    def show_temperature(self):
        if self.ison:
            if self.temperature>=37 and self.temperature<41:
                print("Your temperature:",self.temperature,"(Fever)")
            elif self.temperature>=41:
                print("Your temperature:",self.temperature,"(CRITICAL!)")
            else:
                print("Your temperature:",self.temperature)
        else:
            print("Thermometer is off!")

class Ebook():
    def __init__(self,Author,Title,Number_of_pages,Current_page):
        self.is_opened = False
        self.Author = Author
        self.Title = Title
        self.Number_of_pages = Number_of_pages
        self.Current_page = Current_page

    def open(self):
        self.is_opened = True

    def close(self):
        self.is_opened = False
    
    def next_page(self):
        if self.is_opened:
            if self.Current_page<self.Number_of_pages:
                self.Current_page+=1
            else:
                print("You reached The End")
        else:
            print("You must open a book!")
    
    def previous_page(self):
        if self.is_opened:
            if self.Current_page != 1:
                self.Current_page-=1
            else:
                print("You can't go behind 1st page")
        else:
            print("You must open a book!")
    
    def status(self):
        if self.is_opened:
            print(f"Title: {self.Title}\nAuthor: {self.Author}\nNumber of pages: {self.Number_of_pages}\nCurrent page: {self.Current_page}")
        else:
            print("Book is closed")

class Bank():
    def __init__(self,bankNo):
        self.bankNo = bankNo
        self.balance = 0
    
    def deposit(self,amount):
        self.balance+=amount
    
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
        else:
            print("Insufficient funds on the account")

    def status(self):
        print("Bank Account No:",self.bankNo)
        print("Balance: PLN",self.balance)


class Statistics():
    def __init__(self):
        self.numbers = []

    def greatestnumber(self):
        self.greatest = max(self.numbers)

    def smallestnumber(self):
        self.smallest = min(self.numbers)

    def arithmeticmean(self):
        sum=0
        for i in self.numbers:
            sum+=i
        
        self.mean = sum/len(self.numbers)
    
    def median(self):
        if len(self.numbers)%2 == 0:
            middle1 = self.numbers[int(len(self.numbers)/2)-1]
            middle2 = self.numbers[int(len(self.numbers)/2)]

            self.med = (middle1+middle2)/2
        else:
            self.med = self.numbers[int(len(self.numbers)/2)]

    def addnumber(self):
        x = int(input("Add a number: "))
        self.numbers.append(x)
    
    def status(self):
        print(f"Numbers: {self.numbers}\nGreatest number: {self.greatest}\nSmallest number: {self.smallest}\nArithmetic mean: {self.mean}\nMedian: {self.med}")



        



