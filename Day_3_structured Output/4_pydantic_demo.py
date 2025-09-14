# same here also we make class and validate like if given name to some variable like it is string then it will be string only unlike typeddic
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name : str = 'Kunal Punia'  #by default we can give
    age : Optional[int] = None  #we need to set this if no value then it will print none
    email : EmailStr    #built in function in the pydantic library
    cgpa : float = Field(gt=0,lt=10, description="A decimal value representing the cgpa of student")  #we can even add constraint and can add description also 

 # new_student = {'age':20}  # here we can not pass the integer bcoz there is validation this feature was not there in that typeddic
new_student = {'age':'20','email':'abc@gmail.com','cgpa':5}  # here we can pass string it will be converted into the int

student = Student(**new_student)


# print(type(student)) # pydantic object

# we can convert this into dict also
student_dict = dict(student)
print(student_dict['age'])

# we can convert this into JSON
student_json = student.model_dump_json()