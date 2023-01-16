class University():

    # object constructor (__init__ method)
    def __init__(self):
        # object states/attributes (fields)
        self.name = 'CUE' 
        self.fullname = "Uniwersytet Ekonomiczny w Krakowie"   

    # object bahaviors (methods)
    def print_name(self):  
        print(self.name)

    def print_fullname(self):
        print(self.fullname)

    def set_name(self, name):
        self.name = name
    
    def set_fullname(self,name):
        self.fullname = name

Uni = University()
Uni.print_name()
Uni.print_fullname()
Uni.set_name("MIT")
Uni.set_fullname("Massachusetts Institute of Technology")
Uni.print_name()
Uni.print_fullname()