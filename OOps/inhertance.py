#inhertance use your parent asset(attributes) use child class, 
class persion:                                              #parent class
    def __init__(self,name,age,join_year,tamil, english):   #parent attributes
        self.name=name
        self.age=age
        self.join_year=join_year
        self.tamil=tamil
        self.english=english
    def _12thmark(self):                                     #parent method
        print(f"tamil mark:{self.tamil}")
        print(f"english mark:{self.english}")

class adminsion(persion):                                       #child class
    def __init__(self, name, age, join_year,tamil,english,cource):  #use parent with child attribute
        super().__init__(name, age,join_year,tamil,english)         #super function use parent attribute use child class
        self.cource=cource
    def display(self):                                        # child class method
        print(f"Student name:{self.name}")
        print(f"Student age:{self.age}")
        print(f"Stucent cource:{self.cource}")
        print(f"Student join year:{self.join_year}")
        self._12thmark()                                       #call parent class method


s1=adminsion("vignesh", 22, 2024,97,79,"MCA")                   #object
s1.display()                                                       # object call method from class