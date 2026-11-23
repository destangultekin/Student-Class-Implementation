class Person:
    def __init__(self, age):
        self.age = age

    def get_age(self):
        return self.age
    
class Student(Person):
    def __init__(self, age, id):
        self.id = id
        super().__init__(age)

    def get_gpa(self) -> float:
        return 0.0

class Professor(Person):
    def __init__(self, age, title):
        self.title = title
        super().__init__(age)

    def teach(self) -> None:
        return None

# Test the classes and their methods

student1 = Student(20, "S101")
professor1 = Professor(45, "Doctor")

print(student1.get_age())
print(student1.get_gpa())
print(professor1.get_age())

professor1.teach()