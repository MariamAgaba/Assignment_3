class Person:
    def __init__(self, name, race, colour):
        self.name = name
        self.race = race
        self.colour = colour
    def Self_Person(self):
        print(f'This is {self.name}, {self.race} by race, skin colour is {self.colour}')


class Student(Person):
    def student(self, country):
        self.country = country
        print(f' Student name is {self.name}, {self.race} by race, skin colour is {self.colour} and from {self.country}')

class Lecturer(Person):
    def lecturer(self, tribe):
        self.tribe = tribe
        print(f' lecturer name is {self.name}, {self.race} by race, skin colour is {self.colour} and an {self.tribe} tribe')

person1= Person('Abduljabbar', 'African', 'dark')
person2= Student('Salim', 'Asian', 'brown')
person3= Lecturer('Dr. Humphery', 'American', 'white')
person1.Self_Person()
person2.student('China')
person3.lecturer('Indigeneous')




    


