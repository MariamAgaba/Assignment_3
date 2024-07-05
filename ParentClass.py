class Parent:
    def __init__(self, name, proffession, address):
        self.name = name
        self.proffession = proffession
        self.address = address
    def Main_parent(self):
        print(f'My name is {self.name}, a {self.proffession}, and reside in {self.address}')

class Children(Parent):
    def child(self, marital_status):
        self.marital_status = marital_status
        print(f"My son's name is {self.name}, he is a {self.proffession} and resides in {self.address}. He is {marital_status} and blessed with children")

class Grandchildren(Parent):
    def grandchild(self, education_level):
        self.education_level = education_level
        print(f"My grandchild's name is {self.name}, he is still a {self.proffession} and resides in {self.address}. A {self.education_level} at DLIGHT Academy")

Instance1= Parent("Mariam", "Food Scientist", "Nigeria")
Instance2= Children("Abduljabbar", "doctor","Canada")
Instance3= Grandchildren("Salim","student", "Canada")

Instance1.Main_parent()
Instance2.child("married")
Instance3.grandchild("preschooler")
