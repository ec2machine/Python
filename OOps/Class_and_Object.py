#class ise blueprint use build differnt() buildings,  make objects
class Student:   #class 
    def __init__(self,name,age,english,hindi,tamil):  # consectors
        self.name=name
        self.age=age
        self.english=english
        self.hindi=hindi
        self.tamil=tamil

    def totel_mark(self):                               #methods
        totel=(self.english + self.hindi + self.tamil)
        return totel
    def grade(self):
        value=self.totel_mark()
        match value:
                case value if value >=290:
                    print("Grade:A=")
                case value if value >=250:
                    print("Grade:B")
                case value if value >=200:
                    print("Grade:C")


    
    def display(self):
        print(f"{self.name},\t{self.age}")
        print("=======================")
        print(self.english)
        print(self.hindi)
        print(self.tamil)
        print("=======================")
        print(self.totel_mark())
        print("=======================")
        print(self.grade())


s1=Student("vignesh",22,english=89,hindi=79,tamil=78)   #Object 
s1. display()