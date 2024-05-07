class Person:
    def __init__(self,name:str,age:int) -> None:
        self.name= name
        self.age = age
    def getName(self):
        return self.name


class Student(Person):
    def __init__(self, name: str, age: int, marks:list, grade:str, department:str) -> None:
        super().__init__(name, age)
        self.marks = marks
        self.grade = grade
        self.department = department
    def mainRole(self):
        return "I am a student"
    


s1 = Student("Rana", 23, [80], "A", "Math")

print(f"{s1.name}= {s1.mainRole()}")

class Manager(Person):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)

class CEO(Person):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)