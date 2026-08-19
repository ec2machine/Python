'''
#single
class parent:
    def color(self):
        print("my color is black")
class child(parent):
    def hight(self):
        print("my hight my parent level")
persion1=child()
persion1.color() #acces the parent class 

# persio2=parent()   ==> cant acess child class 
# persio2.hight()
# 
# '''

'''
#multiple inhertance --> two or  more parent but on child
class father:
    def method_father(self):
        print("this is father")

class mother:
    def method_mother(self):
        print("this is mother")

class child(father,mother):
    def method(self):
        self.method_father()
        self.method_mother()

child1=child()
child1.method_father()
child1.method_mother()
child1.method()

'''
'''
#multilevel -> granparent-parent-child
class gran_father:
    def method_gran_father(self):
        print("this is gran father")

class father(gran_father):
    def method_father(self):
        print("this is father")
        self.method_gran_father()

class child(father):
    def method(self):
        self.method_gran_father()
        self.method_father()

child1=child()
child1.method_gran_father()
child1.method_father()
child1.method()

'''
'''
# hieracial inhertance  --one pareent two child
class father:
    def method_father(self):
        print("this is father")

class child1( father):
    def method(self):
        self.method_father()

class child2(father):
    def method(self):
        self.method_father()

child1=child1()
child1.method_father()
child1.method()
child2=child2()
child2.method_father()
child2.method()
'''
'''


Hybrid inheritance
class Person:
    def show_person(self):
        print("I am a person")


class Student(Person):
    def show_student(self):
        print("I am a student")


class Result(Student):
    def show_result(self):
        print("My marks are 90")


class Sports(Student):
    def show_sports(self):
        print("I play cricket")


r = Result()
r.show_person()
r.show_student()
r.show_result()

s = Sports()
s.show_person()
s.show_student()
s.show_sports()

'''

class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog says: Bow Bow")


class Cat(Animal):
    def sound(self):
        print("Cat says: Meow")


a = Animal()
a.sound()

d = Dog()
d.sound()

c = Cat()
c.sound()