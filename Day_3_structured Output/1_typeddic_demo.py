from typing import TypedDict

# making a class which inherits from the typeddic
class Person(TypedDict):
    name : str
    age : int

# creating a obj
new_person: Person = {'name':'Kunal','age':20}

print(new_person)